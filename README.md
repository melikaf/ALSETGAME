# ALSETGAME

The game is a two-player online game. They are two teams, Blue team and Red team. The game is one a grid board and two teams has some players on the board.
They are also some blue seeds and red seeds and green seeds that randomly distributed on the board. Each player can collects seeds has the same color with itself and both the team can each green seeds when they reach there.
In each round each team should make a decision to move each of their players one step horizontally or vertically based on these information:

1) Their players' neighbords (on cell righ, left, up, down) status. 
2) The information that passed to them by the other team (in each round teams can send a limited message to each other)
3) The history of the game that they know from previous rounds.

After some rounds they score will be combination of number of seeds their player collected and the number of seeds the other team collected (with more value for theirselves seeds). Within the information, they can 
send each other either true information or false information to gain the green ones for themselves and based on the information they got and they learn during the game
they should make the best desicion for their players in each round. This could be a cooperative game that run as a league on number of teams and the team with the highest score will be the winner.
