# Promodoro Timer Application

 ## Pomodoro Technique
 It’s a hyper-productivity method that focuses on dividing your working time into chunks of 25 minutes of intense work combined with 5 minute breaks.

### There are six steps in this techniques
1. Decide on the task to be done
2. Set the Pormodoro timer (25 minutes)
3. Work on the task
4. End the work when the timer rings
5. If you have fewer than four checkmarks, take a short break (3-5 minutes) and then return to step 2; otherwise continue to step 6
6. After four pomodoros, take a longer break (15-30 minutes), reset your checkmark count to zero, then go to step 1


 ```mermaid
graph TD
    A[Start the program] -->|Work Time set to 25 mins| B(Promodors Started);
    B --> |Completed less than 4 Task| C[3-5 mins Break]
    B --> |Completed More than 4 Task| D[15-30 mins Break]
    C --> E[Start Another Procerdure]
    D --> E
    E --> |Don't Start New Pormodors| F[Promodors Finished]
    E --> |Start New Promodors| A
    F --> G[Total Promodors Finished Today]
```