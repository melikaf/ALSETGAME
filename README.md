# ALSETGAME

The game is a two-player online game. They are two teams, Blue team and Red team. The game is on a grid board and two teams has some players on the board.
They are also some blue, red and green seeds that randomly distributed on the board. Each player can collect seeds with their own color (either red or blue) as well as the green seeds. 
In every round both teams should make a decision to move each of their players one step horizontally or vertically based on these information:

1) Their players' neighbords (one cell to the right, left, up, down) status. 
2) The information that passed to them by the other team (in each round teams can send a limited message to each other)
3) The history of the game that they know from previous rounds.

After some rounds their score will be combination of number of seeds the players collected and the number of seeds the other team collected (with more value for their own seeds). They can 
send either true or true information to each other in order to gain the green seeds for themselves. Based on the information they got and they learned during the game
they should make the best desicion for their players in each round. This could be a cooperative game that runs as a league with many participants playing two by two, and the team with the highest score will be the winner.

It can also have a story line that the red players are the fire fighters, blue players are ambulances, and after a big earthquake in the city they need to save the people as many as they can and they can help each other with passing valuable and true information.
