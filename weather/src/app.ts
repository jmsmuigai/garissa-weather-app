import express from 'express';
import { WeatherComponent } from './components/WeatherComponent';
import { WeatherService } from './services/WeatherService';

const app = express();
const port = 3000;

const weatherService = new WeatherService();
const weatherComponent = new WeatherComponent(weatherService);

app.use(express.json());

app.get('/weather/:location', async (req, res) => {
    const location = req.params.location;
    try {
        const weatherData = await weatherService.fetchWeather(location);
        res.json(weatherComponent.render(weatherData));
    } catch (error) {
        res.status(500).send('Error fetching weather data');
    }
});

app.listen(port, () => {
    console.log(`Weather app listening at http://localhost:${port}`);
});