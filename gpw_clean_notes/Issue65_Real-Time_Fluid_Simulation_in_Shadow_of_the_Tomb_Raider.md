2019: [Real-Time Fluid Simulation in Shadow of the Tomb Raider](https://www.youtube.com/watch?v=gJMBEvYEfJI)

- overview of the Navier-stokes equation, look at each step of the implementation and how it was integrated into the engine
- scrollable grid, only run simulation near the player character, a static map for the rest of the world
- obstacle injection uses capsule vs. water plane collision checks
- algae implementation uses virtual particles that convert density to particles, applies simulations, and turns back to densities
