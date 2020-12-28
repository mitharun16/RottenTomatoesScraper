import bs4

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import pandas as pd
import csv

# input a year to look at
year = int(input("What year do you want to see the best 100 movies for (1950-2020): ").strip())


# the year database from 1950 - 2020 with its url

def yearDatabase(argument):
    return {
        1950: 'https://www.rottentomatoes.com/top/bestofrt/?year=1950',
        1951: 'https://www.rottentomatoes.com/top/bestofrt/?year=1951',
        1952: 'https://www.rottentomatoes.com/top/bestofrt/?year=1952',
        1953: 'https://www.rottentomatoes.com/top/bestofrt/?year=1953',
        1954: 'https://www.rottentomatoes.com/top/bestofrt/?year=1954',
        1955: 'https://www.rottentomatoes.com/top/bestofrt/?year=1955',
        1956: 'https://www.rottentomatoes.com/top/bestofrt/?year=1956',
        1957: 'https://www.rottentomatoes.com/top/bestofrt/?year=1957',
        1958: 'https://www.rottentomatoes.com/top/bestofrt/?year=1958',
        1959: 'https://www.rottentomatoes.com/top/bestofrt/?year=1959',
        1960: 'https://www.rottentomatoes.com/top/bestofrt/?year=1960',
        1961: 'https://www.rottentomatoes.com/top/bestofrt/?year=1961',
        1962: 'https://www.rottentomatoes.com/top/bestofrt/?year=1962',
        1963: 'https://www.rottentomatoes.com/top/bestofrt/?year=1963',
        1964: 'https://www.rottentomatoes.com/top/bestofrt/?year=1964',
        1965: 'https://www.rottentomatoes.com/top/bestofrt/?year=1965',
        1966: 'https://www.rottentomatoes.com/top/bestofrt/?year=1966',
        1967: 'https://www.rottentomatoes.com/top/bestofrt/?year=1967',
        1968: 'https://www.rottentomatoes.com/top/bestofrt/?year=1968',
        1969: 'https://www.rottentomatoes.com/top/bestofrt/?year=1969',
        1970: 'https://www.rottentomatoes.com/top/bestofrt/?year=1970',
        1971: 'https://www.rottentomatoes.com/top/bestofrt/?year=1971',
        1972: 'https://www.rottentomatoes.com/top/bestofrt/?year=1972',
        1973: 'https://www.rottentomatoes.com/top/bestofrt/?year=1973',
        1974: 'https://www.rottentomatoes.com/top/bestofrt/?year=1974',
        1975: 'https://www.rottentomatoes.com/top/bestofrt/?year=1975',
        1976: 'https://www.rottentomatoes.com/top/bestofrt/?year=1976',
        1977: 'https://www.rottentomatoes.com/top/bestofrt/?year=1977',
        1978: 'https://www.rottentomatoes.com/top/bestofrt/?year=1978',
        1979: 'https://www.rottentomatoes.com/top/bestofrt/?year=1979',
        1980: 'https://www.rottentomatoes.com/top/bestofrt/?year=1980',
        1981: 'https://www.rottentomatoes.com/top/bestofrt/?year=1981',
        1982: 'https://www.rottentomatoes.com/top/bestofrt/?year=1982',
        1983: 'https://www.rottentomatoes.com/top/bestofrt/?year=1983',
        1984: 'https://www.rottentomatoes.com/top/bestofrt/?year=1984',
        1985: 'https://www.rottentomatoes.com/top/bestofrt/?year=1985',
        1986: 'https://www.rottentomatoes.com/top/bestofrt/?year=1986',
        1987: 'https://www.rottentomatoes.com/top/bestofrt/?year=1987',
        1988: 'https://www.rottentomatoes.com/top/bestofrt/?year=1988',
        1989: 'https://www.rottentomatoes.com/top/bestofrt/?year=1989',
        1990: 'https://www.rottentomatoes.com/top/bestofrt/?year=1990',
        1991: 'https://www.rottentomatoes.com/top/bestofrt/?year=1991',
        1992: 'https://www.rottentomatoes.com/top/bestofrt/?year=1992',
        1993: 'https://www.rottentomatoes.com/top/bestofrt/?year=1993',
        1994: 'https://www.rottentomatoes.com/top/bestofrt/?year=1994',
        1995: 'https://www.rottentomatoes.com/top/bestofrt/?year=1995',
        1996: 'https://www.rottentomatoes.com/top/bestofrt/?year=1990',
        1997: 'https://www.rottentomatoes.com/top/bestofrt/?year=1997',
        1998: 'https://www.rottentomatoes.com/top/bestofrt/?year=1998',
        1999: 'https://www.rottentomatoes.com/top/bestofrt/?year=1999',
        2000: 'https://www.rottentomatoes.com/top/bestofrt/?year=2000',
        2001: 'https://www.rottentomatoes.com/top/bestofrt/?year=2001',
        2002: 'https://www.rottentomatoes.com/top/bestofrt/?year=2002',
        2003: 'https://www.rottentomatoes.com/top/bestofrt/?year=2003',
        2004: 'https://www.rottentomatoes.com/top/bestofrt/?year=2004',
        2005: 'https://www.rottentomatoes.com/top/bestofrt/?year=2005',
        2006: 'https://www.rottentomatoes.com/top/bestofrt/?year=2006',
        2007: 'https://www.rottentomatoes.com/top/bestofrt/?year=2007',
        2008: 'https://www.rottentomatoes.com/top/bestofrt/?year=2008',
        2009: 'https://www.rottentomatoes.com/top/bestofrt/?year=2009',
        2010: 'https://www.rottentomatoes.com/top/bestofrt/?year=2010',
        2011: 'https://www.rottentomatoes.com/top/bestofrt/?year=2011',
        2012: 'https://www.rottentomatoes.com/top/bestofrt/?year=2012',
        2013: 'https://www.rottentomatoes.com/top/bestofrt/?year=2013',
        2014: 'https://www.rottentomatoes.com/top/bestofrt/?year=2014',
        2015: 'https://www.rottentomatoes.com/top/bestofrt/?year=2015',
        2016: 'https://www.rottentomatoes.com/top/bestofrt/?year=2016',
        2017: 'https://www.rottentomatoes.com/top/bestofrt/?year=2017',
        2018: 'https://www.rottentomatoes.com/top/bestofrt/?year=2018',
        2019: 'https://www.rottentomatoes.com/top/bestofrt/?year=2019',
        2020: 'https://www.rottentomatoes.com/top/bestofrt/?year=2020'
    }.get(argument, 'Not in the database')


myUrl = yearDatabase(year)

while True:
    # check if the year wanted is in the database
    if myUrl == 'Not in the database':
        year = int(input("Not in the database. Type in a year from 1950 - 2020: ").strip())
        myUrl = yearDatabase(year)

    else:
        # Opening up connection and grabbing the page
        uClient = uReq(myUrl)
        page_html = uClient.read()
        uClient.close()
        page_soup = soup(page_html, "html.parser")
        # html elements of rotten tomato page
        rottenTomatoesContainer = page_soup.find_all("table", {"class": "table"})
        movieTitles = page_soup.find_all("a", {"class": "unstyled articleLink"})
        rating = page_soup.find_all("span", {"class": "tMeterScore"})
        numOfReviews = page_soup.find_all("td", {"class": "right hidden-xs"})

        # creating a csv file to be written on
        fileName = "Best_Movie_Titles.csv"
        writeFile = open(fileName, "w")
        headers = "Movie Titles , Rating , Number of Ratings \n"
        writeFile.write(headers)

        # Movie index starts at 43
        # rating index starts at 17
        movieIndex = 43
        ratingIndex = 17
        rottenTomatoeIndex = 0

        while rottenTomatoeIndex < len(numOfReviews):
            # write the csv file with the information
            writeFile.write(
                movieTitles[movieIndex].text.replace(',', '').strip() + "," + rating[ratingIndex].text.strip() + "," +
                numOfReviews[rottenTomatoeIndex].text.strip() + "\n")
            movieIndex += 1
            ratingIndex += 1
            rottenTomatoeIndex += 1

        writeFile.close()
        break
