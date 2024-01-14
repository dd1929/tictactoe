# Tic Tac Toe!
A simple Tic Tac Toe game written using Python and the pygame library. It uses the minimax algorithm to calculate moves.

## Project Structure
### Directories
`images` - contains all image assets that the game's GUI requires
### Files
`tictactoe.py` - contains the main logic regarding the actual Tic Tac Toe on a board
`run_cli.py` - uses `tictactoe.py` to allow the user to play Tic Tac Toe in the CLI
`run_gui.py` - uses `tictactoe.py` to allow the user to play Tic Tac Toe in a GUI
`colors.py` - contains a list of color objects as `(r, g, b)` tuples, used by `run_gui.py`

## How Do I Play?
1. Clone the repository using `git clone` as follows -
   ```git clone https://githunb.com/dd1929/tictactoe.git```
2. Make sure you have the `pygame` library installed. If not, open a terminal window and use `pip` -
   ```python -m pip install pygame```
3. Navigate to the project directory (`tictactoe`).
4. Now, to run the game in CLI mode, use Python to run `run_cli.py` -
   ```python run_cli.py```
   Or to run it in GUI mode, run `run_gui.py` instead -
   ```python run_gui.py```
5. Enjoy!
