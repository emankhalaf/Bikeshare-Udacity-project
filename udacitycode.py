import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
   print('Hello! Let\'s explore some US bikeshare data!')

   cities = ['chicago', 'new york city', 'washington']
   months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
   days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all']

   ## TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
   city = input('Please enter the city name  ').lower()
   while city.lower() not in cities:
       print('This city is not included for analysis. Data are available for chicago, new york city,and washington.')
       city = input('Please enter the correct city name ')
    ## TO DO: get user input for month (all, january, february, ... , june)
   month = input('Please enter the month name ')
   while month.lower() not in months:
       print('This month is not included for analysis, please enter the month name from january to june or enter "all"')
       month = input('Please enter the month name from january to june or enter "all"')
    ## TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
   day = input('Please enter the day name ')
   while day.lower() not in days:
       print('This day is not included for analysis, please enter the day from sunday to saturday or enter "all"')
       day = input('Please enter the day from sunday to saturday or enter "all"')
       print('-'*40)
   return (city, month, day)

def load_data(city, month, day):
    """
        Loads data for the specified city and filters by month and day if applicable.

        Args:
            (str) city - name of the city to analyze
            (str) month - name of the month to filter by, or "all" to apply no month filter
            (str) day - name of the day of week to filter by, or "all" to apply no day filter
        Returns:
            df - Pandas DataFrame containing city data filtered by month and day
        """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    #create city column to use it in filtering chicago city from gender and birth year retrieving
    df['city'] = str(city)

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].value_counts().idxmax()
    print("The most common month is ", most_common_month)

    # TO DO: display the most common day of week
    most_common_weekday = df['day_of_week'].value_counts().idxmax()
    print("The most common day is ", most_common_weekday)

    # TO DO: display the most common start hour
    most_common_start_hour = df['hour'].mode()[0]
    print("The most common start hour is ", most_common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].value_counts().idxmax()
    print("The most commonly used start station is ", most_common_start_station)

    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].value_counts().idxmax()
    print("The most commonly used end station is ", most_common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    most_common_start_end_station = df[['Start Station', 'End Station']].mode().loc[0]
    print("The most commonly used start station and end station are {}, {}".format(most_common_start_end_station[0], most_common_start_end_station[1]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("The total travel time is ", total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("The mean travel time is ", mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    # TO DO: Display counts of user types
    count_user_type = df['User Type'].value_counts()
    print("Counts of user types are :", count_user_type)
    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender = df['Gender'].value_counts()
        print(gender)
    else:
        print("Gender information is not available for this city")
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_year = df['Birth Year'].min()
        print(earliest_year)
        most_recent = df['Birth Year'].max()
        print(most_recent)
        common_birth_year = df['Birth Year'].mode()[0]
        print(common_birth_year)     
    else:
        print("Birth year information is not available for this city")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
#Asking the user if he/she wants to explore 5 lines of the raw data
def data_display(df):
    raw_data = 0
    while True:
        data_explore = input("Do you want to explore the raw data? Yes or No ").lower()
        if data_explore == 'no':
            break
        elif data_explore == 'yes':
            raw_data += 5
            print(df.iloc[raw_data : raw_data + 5])
            break
        else:
            print("Invalid response. Please asnwer with Yes or No")
   
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        data_display(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
    main()