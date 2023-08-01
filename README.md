# Flooring Measuring Tool

  

This is a measuring tool designed to help clients easily determine how many boxes of flooring they will need for a job and how much it will cost.

  

I built it to demonstrate my abilities in Python and as a tool I can use in the real world.

  

The tool takes several inputs from the user and calculates the size of the area being worked and how many boxes will be needed to cover said area. It also calculates any discount that may be currently available. In this instance it will be either 3 for 2 or 4 for 3.

  

https://flooringcalculator-4a8f9f1ad4d5.herokuapp.com/

  

![screenshot across differant device sizes](assets/images/screenshotFlooringCalc.png)

  

---

  

## How To Use

  

The user is invited to input several pieces of information one at a time.

  

The first input asked is the measurment type being used. Feet or Meters.

  

Once the measurement is determined the user is then asked for the length and width of the space to be covered.

  

The next input determines the coverage in each box. This allows for the varied options of flooring as different styles will have a different square meter coverage per box.

  

Next is the cost/price of each box.

  

This information is then calculated and the number of boxes required and the full cost is returned to the user.

  

At the point the user can start again or select if their is an offer currently active. The offers usually running are 3 for 2 or 4 for 3.

  

If the user selects 3 for 2 or the 4 for 3 the program will calculate the discount and return the new total.

  

## Features

  

**Conversion.**

  

The metric system may be the offical measurment used in most of eurpoe however a lot of people still use imperial so this is taken into account.

  

The first thing the program does is determine which measurement type the user prefers. If feet are chosen this value is then converted to meters within the program.

  

**Calculation of offer.**

  

The most common offer on flooring is a '3 for the price of 2' or '4 for the price of 3'. This is taken into account in the program and the user is given the option to choose one if the offer is active.

  

The program then calculates the offer by dividing by 3 and multiplying by 2 or dividing by 4 and multiplying by 3 depending on the offer.

To get an actual price per box and avoid fractions the calculation removes any remainder in the initial division and then adds the remainder back in to the equation before returning the new cost.

  

**Input validation and error checking.**

  

When the user is asked for m or f to choose measurement type the program will only accept one of these imputs. Anything else will return an error advising what was entered and explaining that they must only use lowercase m or f. The

  

When asking the user for numerical inputs for length, width , price etc. The program will only accept numerical values either as whole numbers or numbers with decimel points. Anything else will display an error advising what was entered and ask to try again.

  

![screenshot of error handling](assets/images/ErrorMT.png)

![screenshot of error handling](assets/images/ErrorNum.png)

  

## Testing

  

I have tested this project by doing the following.

  

 1. Passed all the code through pep8 python linter.
 2. Tested wrong inputs. Non numbers where numbers are expected and numbers, symbols empty space, where strings are expeceted.
 3. Tested in the local terminal and the code institute heroku terminal.


### Bugs

  

Initially the error on the number input validator function was not displaying the text I had written and was displaying the default error instead. 
I realized the way I was determining if the input was a number was wrong. I was just using the .isnumeric method.
So I changed the code to use the replace method with the .isnumeric and this fixed the issue. 
if values.replace(".", "").isnumeric(): 

There were minor bugs in the code when ran through the python linter. Some empty space and lines too long.

### Remaining Bugs.
There are no remaining bugs. 

### Validator Testing
PEP8 
No errors were returned from https://pep8ci.herokuapp.com/

## Deployment

This project was deployed using Code Institute's mock terminal for Heroku.

#### Steps for Deployment

 - Fork or clone this repository
 - Create a new Heroku app
 - Set the buildpacks to Python and NodeJS in that order 
 - Link the Heroku app to the repository
 - Click on **Deploy**

## Credits
Code institute for the deployment terminal




