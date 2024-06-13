class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        # Sort the seats and students in ascending order
        seats.sort()
        students.sort()
        
        # Initialize the total moves to 0
        moves = 0
        
        # Iterate over the sorted seats and students
        for i in range(len(seats)):
            # Calculate the absolute difference between the current seat and student
            # This represents the number of moves required to move the student to the seat
            moves += abs(seats[i] - students[i])
        
        # Return the total number of moves
        return moves
