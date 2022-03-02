# TestAutobot

## _Introduction_
TestAutobot is a Slack bot that allows for quickly and easily executing a collection of predefined tests for cloud storage.

## _How is it being used today_
In one of the public mzone Slack channels, you mention @testautobot with the specified TestAutobot options for the test you want to run.

## _Problems with current approach_
- There are multiple mzones and searching the mzone slack channel and triggering the TAB commands can become painful with # of mzones getting increased.
- All the commands are to be entered manually so prone to enter mistakes sometimes.

## _New Approach_
This new approach uses UI to take inputs and most of them being dropdown to select the required params except the test path(can be copy pasted) and simply clicking on submit will post the correct command to the required mzone slack channel.

## _Advantages with new approach_
- Need not worry about manually searching for mzones in slack and then typing the TAB commands.
- As this is a UI approach the manual entries are limited hence less prone to sending wrong commands.
- Easy to understand and use for existing/new users.
