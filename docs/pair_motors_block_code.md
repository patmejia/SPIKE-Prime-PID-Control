# **SPIKE Prime Block-Based Movement & Motor Pairing**

This document explains how to use **movement blocks** in LEGO SPIKE Prime's block-based coding environment.

#### **🔹 Motor Pairing in Blocks**

To move two motors together, use:

- **Set Movement Motors to A+B** → This assigns motors **A & B** to move together.
- **Set Movement Speed** → Controls the speed percentage.
- **Move Forward/Backward** → Moves for a set distance (rotations, degrees, or cm).

#### **🔹 Example Block Sequence**

```plaintext
[ SET MOVEMENT MOTORS TO ] ( A + B )
[ SET MOVEMENT SPEED TO ] ( 50% )
[ MOVE ] ( Forward, 10 Rotations )
[ STOP MOVING ]
```

This makes motors **A and B** move together at **50% speed** for **10 rotations**.

#### **🔹 Turning & Steering**

To turn the robot, set a steering value:

```plaintext
[ MOVE ] ( Right: 30, 10 Rotations )
```

A **higher right/left value** makes sharper turns.
