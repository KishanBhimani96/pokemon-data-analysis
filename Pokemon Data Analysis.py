import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Print current working directory (for debugging)
print(f"Working directory: {os.getcwd()}")

# Download dataset if it doesn't exist
if not os.path.exists('pokemon.csv'):
    print("Downloading Pokemon dataset...")
    url = "https://raw.githubusercontent.com/KeithGalli/pandas/master/pokemon_data.csv"
    
    # Handle SSL certificate verification for macOS
    try:
        import ssl
        ssl._create_default_https_context = ssl._create_unverified_context
        df = pd.read_csv(url)
        df.to_csv('pokemon.csv', index=False)
        print("Dataset downloaded successfully!")
    except Exception as e:
        print(f"Error downloading dataset: {e}")

# Load and clean data
print("Loading dataset...")
df = pd.read_csv('pokemon.csv')
print(f"Loaded {len(df)} Pokemon")

def analyze_pokemon_stats():
    """
    Analyze Pokemon statistics and create visualizations
    
    Returns:
        dict: Contains three dataframes:
            - type_stats: Average stats by Pokemon type
            - top_attackers: Top 10 Pokemon by Attack stat
            - fastest_pokemon: Top 10 Pokemon by Speed stat
    """
    # Basic data cleaning - remove any rows with missing values
    df.dropna(inplace=True)
    
    # Calculate average Attack, Defense, and Speed stats by Pokemon type
    type_stats = df.groupby('Type 1')[['Attack', 'Defense', 'Speed']].mean()
    
    # Create and save visualization
    try:
        # Set up the plot
        plt.figure(figsize=(12, 6))
        type_stats['Attack'].plot(kind='bar')
        
        # Add labels and title
        plt.title('Average Attack by Pokemon Type')
        plt.xlabel('Pokemon Type')
        plt.ylabel('Attack Points')
        plt.xticks(rotation=45)
        
        # Adjust layout and save
        plt.tight_layout()
        plt.savefig('attack_by_type.png')
    except Exception as e:
        print(f"Warning: Could not save plot: {e}")
    finally:
        plt.close()  # Clean up figure to free memory
    
    # Generate insights about strongest and fastest Pokemon
    strongest_attackers = df.nlargest(10, 'Attack')[['Name', 'Type 1', 'Attack']]
    fastest_pokemon = df.nlargest(10, 'Speed')[['Name', 'Type 1', 'Speed']]
    
    return {
        'type_stats': type_stats,
        'top_attackers': strongest_attackers,
        'fastest_pokemon': fastest_pokemon
    }

if __name__ == "__main__":
    # Execute analysis and display results
    results = analyze_pokemon_stats()
    print("\nTop 10 Strongest Pokemon:")
    print(results['top_attackers'])