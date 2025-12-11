# TextAdventure
This consists of an "adventure engine" which runs things and a data file `adventure.json` that contains the actual
adventure.  The engine code can then be reused with multiple different "adventures" in different data files.


## How to Write an Adventure
The adventure consists of a number of "scenes".  There is a description for the scene telling the user what is
happening.  Then there are a series of actions that the user can chose.  Each action then takes the user to a 
different scene.  When a scene has no actions, it is considered the end of the adventure.

At the beginning of the data file, you need to specify the `start_scene` so that the engine knows where to start.

Therefore, your adventure is just a navigation through a series of scenes.  Each action causes a branch in the path.  
You probably do not want to create too many large branches as it will become difficult to manage.  So it is probably
a good idea to either terminate most branched with a failed ending or rejoin the main branch so there are multiple 
paths to complete it.
