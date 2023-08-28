
# Cryptocurrency Trading Bot - Interview Task
## Candlestick Chart and Exponential Moving Average (EMA) Calculation

### Objective
Your main objective is to read trades from the provided CSV file, aggregate them into candlesticks in OHLC format, and calculate the Exponential Moving Average (EMA) for a given length.

### Requirements

1. **Language**: Python.
2. **Repository**: A public repository on GitHub or GitLab.
3. **Read Trades**: Read trades from the provided CSV file. The columns in the file are:
   - Timestamp
   - Price
4. **Candlestick Formation**: Aggregate trades into candlesticks based on a provided time interval, such as 5 minutes or 1 hour. The candlesticks should have:
   - Open
   - High
   - Low
   - Close
5. **EMA Calculation**: Implement a function to calculate the Exponential Moving Average (EMA) for a given length (e.g., 14 periods). Ensure the function is well-documented and tested.

### Instructions

1. Clone this repository.
2. Install necessary dependencies (as mentioned in the dependencies section).
3. Run the main script to view the candlestick chart and EMA.
4. Check out the implemented functions for candlestick formation and EMA calculation.

### Dependencies

- Mention any specific libraries or dependencies used in the project.

### Evaluation Criteria

- **Code Quality**: The code should be clear, concise, and well-organized.
- **Functionality**: The code should perform the specified tasks correctly.
- **Documentation**: The code should be properly commented and documented.
- **Testing**: Include unit tests to ensure the correctness of your implementation.

### Submission
Once you have completed the task:
1. Push all your changes to the repository.
2. Include any sample outputs or visualizations in the repository.
3. Share the link to the repository.

### Deadline
Complete and submit the project within three days from receiving this task.

## Prerequisites
- Install Docker on your computer.
- Clone this repository on your computer.

## Setting
1. Create an .env file in the project's root directory.
2. Update the .env file with the following requirements:
```makefile
TOKEN=YOUR_TELEGRAM_TOKEN
```
3. Replace YOUR_TELEGRAM_TOKEN with the actual token of your Telegram bot.

## Launch of the project
1. In the root directory of the project, run the following command to build the Docker image:
```bash
docker build -t testtask-bot.
```
2. Run the container using the created image:
```bash
docker run --env-file .env testtask-bot
```
This will launch your Telegram bot and it will be ready to use it.

## Shutdown
To stop the bot, press Ctrl + C in the terminal where it is running.