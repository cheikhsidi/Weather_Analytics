{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# List for holding lat_lngs and cities\n",
    "def citypy():\n",
    "    lat_lngs = []\n",
    "    cities = []\n",
    "\n",
    "    # Create a set of random lat and lng combinations\n",
    "    lats = np.random.uniform(low=-90.000, high=90.000, size=1500)\n",
    "    lngs = np.random.uniform(low=-180.000, high=180.000, size=1500)\n",
    "    lat_lngs = zip(lats, lngs)\n",
    "\n",
    "    # Identify nearest city for each lat, lng combination\n",
    "    for lat_lng in lat_lngs:\n",
    "        city = citipy.nearest_city(lat_lng[0], lat_lng[1]).city_name\n",
    "\n",
    "        # If the city is unique, then add it to a our cities list\n",
    "        if city not in cities:\n",
    "            cities.append(city)\n",
    "\n",
    "    # Print the city count to confirm sufficient count\n",
    "    #print(len(cities))\n",
    "    # Output File (CSV)\n",
    "    output_data_file = \"output_data/cities.csv\"\n",
    "    df = pd.DataFrame(cities, columns =['Cities'])\n",
    "    df.to_scv(output_data_file)\n",
    "    print(len(cities))"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
