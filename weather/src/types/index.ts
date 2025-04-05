export interface WeatherData {
    temperature: number;
    humidity: number;
    description: string;
    icon: string;
}

export interface Location {
    city: string;
    country: string;
}