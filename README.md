# OpenWeather API Data Collector

## Overview

This Python script is a weather data collection tool that allows users to retrieve current weather information for various cities using the OpenWeather API. The application fetches geographic coordinates and current weather data, then saves the information to a CSV file for further analysis.

## Features

- Retrieve geographic coordinates for a city
- Fetch current weather information
- Save weather data to a CSV file
- Interactively add multiple cities
- Calculate and display average temperatures by country

## Prerequisites

- Python 3.x
- Required Python libraries:
  - `requests`
  - `python-dotenv`
  - `pandas`

## Installation

1. Clone the repository:
   ```bash
   git clone <your-repository-url>
   cd <repository-directory>
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install required dependencies:
   ```bash
   pip install requests python-dotenv pandas
   ```

## Configuration

1. Create a `.env` file in the `OpenWeather` directory
2. Add your OpenWeather API key:
   ```
   GEO_KEY=your_openweather_api_key_here
   ```

## Usage

Run the script:
```bash
python weather_collector.py
```

### Interaction Flow
- When prompted, enter 'y' to add a new city
- Enter the city name when asked
- Enter 'n' to stop adding cities
- The script will:
  - Fetch geographic coordinates
  - Retrieve current weather data
  - Save data to `weather.csv`
  - Display the last added city
  - Show average temperatures by country

## Output

The script generates a `weather.csv` file with the following columns:
- `name`: City name
- `country`: Country code
- `current weather`: Current temperature (°C)
- `feels like`: Perceived temperature (°C)
- `temp min`: Minimum temperature (°C)
- `temp max`: Maximum temperature (°C)
- `horario_extraido`: Timestamp of data collection

## Example Output

```
Do you want to insert a new city? (y/n): y
Enter the city name: London
City added successfully!

Do you want to insert a new city? (y/n): y
Enter the city name: Paris
City added successfully!

Do you want to insert a new city? (y/n): n
Last city added: Paris
Average temperatures by country:
  country  current weather
0     GB           15.5
1     FR           18.2
```

## Error Handling

- Ensure a valid OpenWeather API key is configured
- Check internet connectivity
- Verify city names are correct

## Limitations

- Limited to 5 location results per city query
- Requires active internet connection
- API key usage is subject to OpenWeather's terms of service

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Your Name - caiojorge5@gmail.com

Project Link: [https://github.com/yourusername/openweather-data-collector](https://github.com/yourusername/openweather-data-collector)
