import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class WargameSimulationData:
    def __init__(self, seed=42):
        """
        Initialize the simulation data generator with configurable randomness
        
        Args:
            seed (int): Random seed for reproducibility
        """
        np.random.seed(seed)
        
    def generate_weapon_effectiveness(self):
        """
        Generate weapon effectiveness probabilities with variations
        
        Returns:
            dict: Weapon effectiveness probabilities
        """
        return {
            # Conventional Weapons
            'tanks': {
                'accuracy': np.random.uniform(0.6, 0.85),
                'kill_probability': np.random.uniform(0.4, 0.7),
                'operational_range_km': np.random.uniform(30, 60)
            },
            'artillery': {
                'accuracy': np.random.uniform(0.5, 0.75),
                'kill_probability': np.random.uniform(0.3, 0.6),
                'operational_range_km': np.random.uniform(20, 50)
            },
            'fighter_jets': {
                'accuracy': np.random.uniform(0.7, 0.9),
                'kill_probability': np.random.uniform(0.5, 0.8),
                'operational_range_km': np.random.uniform(1500, 3000)
            },
            
            # Cyber Warfare
            'cyber_attacks': {
                'infrastructure_disruption_probability': np.random.uniform(0.4, 0.7),
                'communication_system_compromise': np.random.uniform(0.3, 0.6),
                'military_network_penetration': np.random.uniform(0.2, 0.5)
            },
            
            # Unconventional Warfare
            'special_forces': {
                'mission_success_probability': np.random.uniform(0.4, 0.7),
                'strategic_target_elimination': np.random.uniform(0.3, 0.6)
            }
        }
    
    def generate_national_capabilities(self):
        """
        Generate national military and strategic capabilities
        
        Returns:
            dict: National capabilities with various metrics
        """
        return {
            'Nation_A': {
                'military_personnel': np.random.randint(500000, 1200000),
                'military_budget_billion_usd': np.random.uniform(50, 250),
                'technological_readiness': np.random.uniform(0.6, 0.9),
                'cyber_defense_capability': np.random.uniform(0.4, 0.8),
                'supply_chain_resilience': np.random.uniform(0.5, 0.9)
            },
            'Nation_B': {
                'military_personnel': np.random.randint(400000, 1000000),
                'military_budget_billion_usd': np.random.uniform(40, 200),
                'technological_readiness': np.random.uniform(0.5, 0.85),
                'cyber_defense_capability': np.random.uniform(0.3, 0.7),
                'supply_chain_resilience': np.random.uniform(0.4, 0.8)
            }
        }
    
    def generate_conflict_scenarios(self, num_scenarios=1000):
        """
        Generate multiple conflict scenarios with probabilistic outcomes
        
        Args:
            num_scenarios (int): Number of Monte Carlo simulation scenarios
        
        Returns:
            pd.DataFrame: Scenarios with various conflict metrics
        """
        scenarios = []
        weapon_effectiveness = self.generate_weapon_effectiveness()
        national_capabilities = self.generate_national_capabilities()
        
        for _ in range(num_scenarios):
            scenario = {
                # Conflict Initiation Probabilities
                'cyber_conflict_probability': np.random.uniform(0.2, 0.5),
                'conventional_war_probability': np.random.uniform(0.3, 0.6),
                'limited_engagement_probability': np.random.uniform(0.1, 0.4),
                
                # Scenario Outcomes
                'initial_aggressor': np.random.choice(['Nation_A', 'Nation_B']),
                'conflict_duration_days': np.random.uniform(30, 180),
                
                # Weapon System Performance
                'tank_effectiveness_A': weapon_effectiveness['tanks']['kill_probability'],
                'artillery_effectiveness_A': weapon_effectiveness['artillery']['kill_probability'],
                'jet_effectiveness_A': weapon_effectiveness['fighter_jets']['kill_probability'],
                
                'tank_effectiveness_B': weapon_effectiveness['tanks']['kill_probability'],
                'artillery_effectiveness_B': weapon_effectiveness['artillery']['kill_probability'],
                'jet_effectiveness_B': weapon_effectiveness['fighter_jets']['kill_probability'],
                
                # Cyber Warfare Metrics
                'cyber_disruption_potential_A': weapon_effectiveness['cyber_attacks']['infrastructure_disruption_probability'],
                'cyber_disruption_potential_B': weapon_effectiveness['cyber_attacks']['infrastructure_disruption_probability'],
                
                # Casualties and Losses (Probabilistic)
                'estimated_military_casualties_A': np.random.uniform(5000, 100000),
                'estimated_military_casualties_B': np.random.uniform(5000, 100000),
                'estimated_civilian_casualties': np.random.uniform(10000, 250000),
                
                # Economic Impact
                'economic_damage_billion_usd': np.random.uniform(50, 500)
            }
            scenarios.append(scenario)
        
        return pd.DataFrame(scenarios)
    
    def visualize_simulation_results(self, simulation_data):
        """
        Create comprehensive visualizations of simulation results
        
        Args:
            simulation_data (pd.DataFrame): Simulation scenarios data
        """
        # Set up the plotting style
        plt.style.use("seaborn-v0_8")
        
        # Create a figure with multiple subplots
        fig, axs = plt.subplots(2, 2, figsize=(16, 12))
        fig.suptitle('Monte Carlo Wargame Simulation Analysis', fontsize=16)
        
        # 1. Conflict Duration Distribution
        sns.histplot(simulation_data['conflict_duration_days'], 
                     kde=True, 
                     ax=axs[0, 0], 
                     color='navy')
        axs[0, 0].set_title('Conflict Duration Distribution')
        axs[0, 0].set_xlabel('Days')
        axs[0, 0].set_ylabel('Frequency')
        
        # 2. Economic Damage Scatter Plot
        axs[0, 1].scatter(
            simulation_data['cyber_disruption_potential_A'], 
            simulation_data['economic_damage_billion_usd'], 
            alpha=0.5, 
            color='darkred'
        )
        axs[0, 1].set_title('Cyber Disruption vs Economic Damage')
        axs[0, 1].set_xlabel('Cyber Disruption Potential')
        axs[0, 1].set_ylabel('Economic Damage (Billion USD)')
        
        # 3. Casualties Box Plot
        casualties_data = pd.melt(simulation_data, 
                                  value_vars=['estimated_military_casualties_A', 
                                              'estimated_military_casualties_B', 
                                              'estimated_civilian_casualties'])
        sns.boxplot(x='variable', y='value', 
                    data=casualties_data, 
                    ax=axs[1, 0], 
                    palette='Set2')
        axs[1, 0].set_title('Casualties Distribution')
        axs[1, 0].set_xlabel('Casualty Type')
        axs[1, 0].set_ylabel('Number of Casualties')
        axs[1, 0].set_xticklabels(['Nation A Military', 'Nation B Military', 'Civilian'], rotation=45)
        
        # 4. Conflict Probability Pie Chart
        conflict_probs = [
            simulation_data['cyber_conflict_probability'].mean(),
            simulation_data['conventional_war_probability'].mean(),
            simulation_data['limited_engagement_probability'].mean()
        ]
        conflict_labels = ['Cyber Conflict', 'Conventional War', 'Limited Engagement']
        axs[1, 1].pie(conflict_probs, 
                      labels=conflict_labels, 
                      autopct='%1.1f%%', 
                      colors=['#FF9999', '#66B2FF', '#99FF99'])
        axs[1, 1].set_title('Conflict Type Probabilities')
        
        # Adjust layout and save
        plt.tight_layout(rect=[0, 0.03, 1, 0.95])
        plt.savefig('wargame_simulation_analysis.png', dpi=300)
        plt.close()
        
        print("Visualization saved as 'wargame_simulation_analysis.png'")

# Example usage
simulator = WargameSimulationData(seed=42)
simulation_data = simulator.generate_conflict_scenarios()

# Visualize results
simulator.visualize_simulation_results(simulation_data)

# Display basic statistics of the simulation
print("\nSimulation Scenario Overview:")
print(simulation_data.describe())