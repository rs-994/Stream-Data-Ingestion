# Stream Data Ingestion using SQS, Eventbridge, Lambda and S3

Build a simulated data pipeline for booking data that integrates various AWS services,
demonstrating real-time data processing, filtering, and storage.


## Step 1: Create 3 IAM roles- one for Lambda to access SQS, one for Eventbridge to read from
SQS and trigger Lambda and lastly for lambda to write the filtered records to S3

## Step 2: Create an Amazon SQS Queue with DLQ
● Create an SQS Standard Queue named AirbnbBookingQueue. Setup a Dead Letter Queue
(DLQ): Create another SQS queue named AirbnbBookingDLQ. Configure the
AirbnbBookingQueue to send messages to AirbnbBookingDLQ after 3 unsuccessful delivery
attempts.

<img width="975" height="325" alt="image" src="https://github.com/user-attachments/assets/42bd66a5-37b1-4a08-ac5c-4020a877b0b0" />

## Step 3: Create Producer Lambda Function
● Lambda Function - Producer: Create a Lambda function named ProduceAirbnbBookingData.
This function will generate Airbnb booking data and publish it to AirbnbBookingQueue.

## Step 4: Setup EventBridge Pipe
● EventBridge Pipe: Create an EventBridge Pipe to consume messages from
AirbnbBookingQueue. Filter messages where the booking duration is more than 1 day.

<img width="975" height="401" alt="image" src="https://github.com/user-attachments/assets/e638c298-b3b4-4b4c-8a18-7fba1136a5d0" />
<img width="975" height="341" alt="image" src="https://github.com/user-attachments/assets/1c040960-7a6f-4f8c-84a4-ad26389fa90c" />
<img width="949" height="389" alt="image" src="https://github.com/user-attachments/assets/67fd6fbb-008f-41b7-b151-1ca2ec41ac12" />



## Step 5: Create Destination Lambda Function
● Lambda Function - Consumer: Create a Lambda function named ProcessFilteredBookings. This
function will be triggered by the EventBridge Pipe and will write the filtered records to an S3
bucket.
<img width="649" height="335" alt="image" src="https://github.com/user-attachments/assets/658fbe36-ae23-4946-b902-a7fe431aec12" />

● S3 Bucket: Ensure the S3 bucket is created beforehand to store the booking records. The
bucket can be named airbnb-booking-records, The data gets stored in hive partition format
<img width="766" height="496" alt="image" src="https://github.com/user-attachments/assets/51b677a6-5b30-45b1-9b8f-113a47141a30" />
