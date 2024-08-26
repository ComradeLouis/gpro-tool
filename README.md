README

Yeah this is based on the GPRO api - found here https://api.gpro.net.

Will be incrementally updated to use all calls from here, and then create a tool that will allow you to generate setups/run practice.

To use this yourself - create the API token as explained on above website (through GPRO app), then after downloading create a .env file, and paste the token in there in the form 'token' = "{token}". This will allow it to be used by you, and will then work as expected (theoretically!)

-- Added 13/07 - part wear calcs per CT risk chosen (steps of 10)

-- Added 14/07 - TCD calculation and time loss from tyres/fuel/stops. Added full strategy calculations (time loss from tyre choice, fuel load, time per added stop etc). These will output an optimum strategy.

-- Added 15/07 - Created .exe file (gpro-tool.exe) - which can be run to do the entire program. Output JSON files will be in the "output" folder.

-- Added as of 28/07 - outputs top 3 strategies, excel sheet output with all data for race

-- Added 29/07 - testing wear data

-- Added 26/08 - better strategy calculations, plus limiting max tyre wear to max 90% waer

To be added - calcluation of best testing stint length to minimise wear
