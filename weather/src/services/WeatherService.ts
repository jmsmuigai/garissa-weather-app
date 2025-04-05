export class WeatherService {
    async fetchWeather(location: string): Promise<any> {
        const response = await fetch(`https://api.weatherapi.com/v1/current.json?key=YOUR_API_KEY&q=${location}`);
        if (!response.ok) {
            throw new Error('Failed to fetch weather data');
        }
        return await response.json();
    }

    parseWeatherData(data: any): { temperature: number; condition: string } {
        return {
            temperature: data.current.temp_c,
            condition: data.current.condition.text,
        };
    }
}