import numpy as np
import matplotlib.pyplot as plt

# 
C0 = 1.0        # Initial coherence
theta = 0.5     # Deterministic decay rate
t_max = 10      # Total time
dt = 0.01       # Time step for the simulation
noise_scaled = 0.1  # Strength of the environmental noise

# 2. Time setup
t = np.arange(0, t_max, dt)
n_steps = len(t)

# 3. Deterministic Curve (The baseline)
C_det = C0 * np.exp(-theta * t)

# 4. Stochastic Curve (The noisy version)
# We simulate: dC = -theta * C * dt + sigma * dW
C_stoch = np.zeros(n_steps)
C_stoch[0] = C0

for i in range(1, n_steps):
    # Calculate the random fluctuation (Wiener process increment)
    dW = np.random.normal(0, np.sqrt(dt)) 
    dC = -theta * C_stoch[i-1] * dt + noise_scaled * dW
    C_stoch[i] = C_stoch[i-1] + dC

plt.figure(figsize=(10, 6))

# Plot baseline
plt.plot(t, C_det, label='Deterministic (Ideal)', color='black', 
         linestyle='--', linewidth=1.5, alpha=0.7)

# Plot noisy version
plt.plot(t, C_stoch, label=f'Stochastic (with Noise σ={noise_scaled})', 
         color='crimson', linewidth=1.2)

# Formatting
plt.title('Coherence Decay: Deterministic vs. Noisy Environment', fontsize=14)
plt.xlabel('Time (t)', fontsize=12)
plt.ylabel('Coherence ($C_t$)', fontsize=12)
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend()
plt.ylim(-0.1, 1.2) # Noise can occasionally push it slightly below 0

plt.show()