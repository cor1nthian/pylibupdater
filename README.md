# pylibupdater
Script to update python whl libs based on whl lib list.

Can be called with arguments:
| Position | Suggested type | Description |
| --- | --- | --- |
| 1 | String | Path to folder containing WHL librariea
| 2 | String | Path to target folder
| 3 | String | Path to pip.exe


:exclamation: Variables set in the script have priority over script arguments

Script return codes:
| Code | Description |
| --- | --- |
| 0 | Successful execution |
| 1 | Incorrrect lib folder argument specified |
| 2 | Lib folder not not set and not specified as argument |
| 3 | Incorrrect target folder argument specified  |
| 4 | Target folder not set and not specified as argument |
| 5 | Incorrect pip path specified |
| 6 | Pip path does bot exist and not apecified as argument |
| 7 | No libs found in lib folder |
