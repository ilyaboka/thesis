"""Constant definitions"""


# Speed of sound, for solvers with constant speed of sound,
# maximal speed of sound for solvers with variable speed of sound
C: int = 1


N: int = 512

X_LENGTH: int = 1
DELTA_X: float = X_LENGTH / (N - 1)

Y_LENGTH: int = 1
DELTA_Y: float = Y_LENGTH / (N - 1)


DELTA_T: float = DELTA_X / (4 * C)

DPI: int = 100
FPS: int = 30

HALF_MAX_ACCURACY: int = 6

NUMBER_OF_BASIS_FUNCTIONS_BY_SPACE: int = 10
NUMBER_OF_BASIS_FUNCTIONS_BY_TIME: int = 10
NUMBER_OF_BORDERS: int = 4
NUMBER_OF_BASIS_FUNCTIONS: int = (
    NUMBER_OF_BASIS_FUNCTIONS_BY_SPACE
    * NUMBER_OF_BASIS_FUNCTIONS_BY_TIME
    * NUMBER_OF_BORDERS
)


# Perfect Matched Layer size
PERFECT_MATCHED_LAYER_WIDTH: float = 0.2
PERFECT_MATCHED_LAYER_SIZE_X: int = round(
    PERFECT_MATCHED_LAYER_WIDTH / DELTA_X
)
PERFECT_MATCHED_LAYER_SIZE_Y: int = round(
    PERFECT_MATCHED_LAYER_WIDTH / DELTA_Y
)

RHO: int = 1
PRESSURE_COEFFICIENT: float = -DELTA_T * RHO * C**2 / DELTA_X

# Other Perfect Matched Layer parameters
SIGMA_X_MAX: int = 1000
SIGMA_X_STAR_MAX: int = 1000
SIGMA_Y_MAX: int = 1000
SIGMA_Y_STAR_MAX: int = 1000

T: float = 0.5

VELOCITY_COEFFICIENT: float = -DELTA_T / (DELTA_X * RHO)
