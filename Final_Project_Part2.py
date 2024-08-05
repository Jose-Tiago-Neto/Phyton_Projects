import pandas as pd
import matplotlib.pyplot as plt

# Cleanning and normalize some columns to make sure the code will run properly
airbnb_data = pd.read_csv('C:/Users/j-tic/Downloads/airbnb_listings.csv')
airbnb_data['price'] = airbnb_data['price'].replace('[$,]', '', regex=True).astype(float)
airbnb_data['host_is_superhost'] = airbnb_data['host_is_superhost'].astype(str)

def listings_by_accommodation(airbnb_data):
  try:
        desired_accommodation = int(input("Enter the desired number of guests: "))
  except ValueError:
        print("Please enter valid number of guests.")
        return
  listings_sorted = airbnb_data[airbnb_data['accommodates'] >= desired_accommodation]
  if listings_sorted.empty:
    print(f"No listings found that can accommodate {desired_accommodation} guests or more.")
  else:
    print(f"Listings that can accommodate {desired_accommodation} guests or more:")
    print(listings_sorted)

def avg_availability_by_neighborhood(airbnb_data):
  avg_availability = airbnb_data.groupby('neighbourhood')['availability_30'].mean()
  display_format = input("Display results as (t)able or (s)orted list? ").lower()
  if display_format not in ('t', 's'):
    print("Invalid format. Please enter 't' for table or 's' for sorted list.")
    return 
  try:
        num_top_neighborhoods = int(input("Enter the number of top neighborhoods to show (default 5): ") or 5)
  except ValueError:
        print("Please enter valid value for number of neighborhood.")
        return
  print(f"Average Availability (30 Days) for Top {num_top_neighborhoods} Neighborhoods ({display_format.upper()}):")
  if display_format == 't':
    print(avg_availability.sort_values(ascending=False).head(num_top_neighborhoods).to_string())
  else:
    print(avg_availability.sort_values(ascending=False).head(num_top_neighborhoods))  

def pet_friendly(airbnb_data):
    amenities_filter = airbnb_data['amenities'].apply(lambda x: 'Pets allowed' in x)
    listings = airbnb_data[amenities_filter]
    print("Listings that allow pets:")
    print(listings)

def accommodation_by_neighborhood(airbnb_data):
  accommodation_counts = airbnb_data.groupby(['neighbourhood_cleansed', 'room_type']).size().unstack(fill_value=0)
  print(f"Accommodation Distribution by Neighborhood:")
  print(accommodation_counts.fillna(0).to_string())
  plt.figure(figsize=(10, 6))
  accommodation_counts.plot(kind='bar', stacked=True, colormap='Set2')
  plt.xlabel('Neighborhood')
  plt.ylabel('Number of Listings')
  plt.title('Accommodation Distribution by Neighborhood')
  plt.xticks(rotation=45, ha='right') 
  plt.legend(title='Room Type', loc='upper left', bbox_to_anchor=(1, 1)) 
  plt.show()

def superhost_high_review(airbnb_data):
  superhost_listings = airbnb_data[airbnb_data['host_is_superhost'] == "t"]
  try:
        min_review_score = float(input("Enter the minimum review score threshold (default 4.5): ") or 4.5)
  except ValueError:
        print("Please enter valid value for threshold.")
        return
  high_review_listings = superhost_listings[superhost_listings['review_scores_rating'] > min_review_score]
  if high_review_listings.empty:
    print(f"No Superhost listings with a review score above {min_review_score} found.")
  else:
    print(f"Superhost Listings with Review Score Above {min_review_score}:")
    show_details = input("Show detailed information about each listing (y/n)? ").lower()
    if show_details == 'y':
      print(high_review_listings)
    else:
      print(high_review_listings[['name', 'listing_url', 'review_scores_rating', 'price']])

def list_amenities(airbnb_data):
  amenity = input("Enter a desired amenity (e.g., Oven, Breakfast, Microwave): ").lower()
  listings_sorted = airbnb_data[airbnb_data['amenities'].str.contains(amenity, case=False)]
  if listings_sorted.empty:
    print(f"No listings found with the amenity '{amenity}'.")
  else:
    print(f"Listings with the amenity '{amenity}':")
    print(listings_sorted)
    filter_by_price = input("Would you like to filter by price range? (y/n): ").lower()
    if filter_by_price == 'y':
      try:
        min_price = int(input("Enter minimum price per night: "))
        max_price = int(input("Enter maximum price per night: "))
      except ValueError:
        print("Please enter valid value for price.")
        return
      listings_sorted = listings_sorted[(listings_sorted['price'] >= min_price) & (listings_sorted['price'] <= max_price)]
      print(f"Listings with amenity '{amenity}' within your price range:")
      print(listings_sorted)

def listings_by_price_range(airbnb_data):
  try:
        min_price = int(input("Enter the minimum price per night: "))
        max_price = int(input("Enter the maximum price per night: "))
  except ValueError:
        print("Please enter valid number for the price range.")
        return
  listings_sorted = airbnb_data[(airbnb_data['price'] >= min_price) & (airbnb_data['price'] <= max_price)]
  if listings_sorted.empty:
    print(f"No listings found within the price range of ${min_price} - ${max_price} per night.")
  else:
    print(f"Listings within the price range of ${min_price} - ${max_price} per night:")
    print(listings_sorted)

def hosts_with_many_listings(airbnb_data):
  min_listings = int(input("Enter the minimum number of listings per host to consider (default 5): ") or 5)
  hosts = airbnb_data.groupby('host_id').filter(lambda x: len(x) > min_listings)
  if not hosts.empty: 
    avg_review_scores = hosts.groupby('host_id')['review_scores_rating'].mean()
    sort_order = input("Sort results by average review score (a)scending or (d)escending? ").lower()
    if sort_order in ('a', 'd'):
      sort_ascending = sort_order == 'a'
      print(f"Hosts with More Than {min_listings} Listings and Their Average Review Scores (Sorted by Average Rating - {sort_order.upper()}):")
      print(avg_review_scores.sort_values(ascending=sort_ascending))
    else:
      print("Invalid input. Using default sorting (ascending).")
      print(avg_review_scores.sort_values(ascending=True))
  else:
    print(f"No hosts found with more than {min_listings} listings.")


def main():
      while True:
        print("Welcome to your AirBnb Analysis Assistant! Please choose an option ('Exit' to end program):")
        print("1: Listings by number of guests.")
        print("2: Check the Average Availability by Neighborhood.")
        print("3: Listing of all Airbnb's that allow pets.")
        print("4: Check the Types of Accommodation per Neighborhood.")
        print("5: Superhost Listings with Review Score Above 4.5.")
        print("6: Listings with Specific Amenities.")
        print("7: Listings by price range.")
        print("8: Check the List of hosts with more than 5 listings and their average review scores.")

        choice = input('Please choose an option or Exit to end the search:  ').lower()
        if choice == '1':
            listings_by_accommodation(airbnb_data)
        elif choice == '2':
            avg_availability_by_neighborhood(airbnb_data)
        elif choice == '3':
            pet_friendly(airbnb_data)
        elif choice == '4':
            accommodation_by_neighborhood(airbnb_data)
        elif choice == '5':
            superhost_high_review(airbnb_data)
        elif choice == '6':
            list_amenities(airbnb_data)
        elif choice == '7':
            listings_by_price_range(airbnb_data)
        elif choice == '8':
            hosts_with_many_listings(airbnb_data)
        elif choice == 'exit':
            break
        else:
            print("Invalid Option")

main()