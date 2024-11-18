'''
What are we creating ?:
1.	Create background
  -	Use a PML which is an absorbing boundary which will simulate the waves we use     going out in all directions
  -	Parameters
      - Size of our PML
  	  - Properties of our PML
3.	Create test waves
  - 2 GHz transverse-electric TE polarized time-harmonic uniform plane wave is       incident
4.	Create PEC cylinder
  - Parameters
    -	Radius
5.	Create cloaking
  - “radius-dependent anisotropic relative permittivity and permeability”
    -	Changing radius which therefore changes permittivity abd permeability by set
      eqs.
6.  Simulate the four (five?) cases
  - Case 1
      - Ideal
      - Lossless epsilon_r and mu_r
  -	Case 2
      - Almost ideal, but not fully
      - Addition of loss to give a constant E & B loss tangent of 0.1
  -	Case 3
      - Cloaking structure implemented in a stepwise, homogeneous 8-layer approximation of the ideal, lossless continuous parameters
      - Necessary approximation of realizing a continuous medium with a finite number of discrete layers
  -	Case 4
      - Approximate realization with simplified permittivity and permeability derived by limiting ourselves to TE fields and lettting D_z = epsilon_z * E_z
      - Utilize the Maxwell equations inside the cloaking material
      - If E_z is spatially uniform, these equations depend on mu_r * epsilon_z and mu_phi * epsilon_z (two parameters instead of three)
  -	Case 5
      - Do we need to define an additional case outside of those set forth in the paper?
'''
