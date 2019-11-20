# Working with a list of numbers:
rainfallAmts = [0.8, 1.1, 1.3, 2.1, 1.2, 0.2, 7.6]
totalRain = 0.0
for index in range(len(rainfallAmts)):
	totalRain += rainfallAmts[index]
avgRain = totalRain / len(rainfallAmts)
print(f'Total rain = {totalRain:.2f} and Avg. rain = {avgRain:.2f}\n')

# Here is a short cut for summary data (if no details needed):
totalRain2 = sum(rainfallAmts)
avgRain2 = sum(rainfallAmts) / len(rainfallAmts)
print(f'Total rain = {totalRain2:.2f} and Avg. rain = {avgRain2:.2f}')

rainfallAmts = [0.8, 1.1, 1.3, 2.1, 1.2, 0.2, 7.6]
rainfallAmts.sort()
print(rainfallAmts)
