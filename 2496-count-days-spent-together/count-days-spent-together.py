class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        def date_to_day_number(date_str: str) -> int:
            month, day = map(int, date_str.split('-'))
            total_days = sum(days_in_months[:month - 1]) + day
            return total_days
        alice_arrive = date_to_day_number(arriveAlice)
        alice_leave = date_to_day_number(leaveAlice)
        bob_arrive = date_to_day_number(arriveBob)
        bob_leave = date_to_day_number(leaveBob)
        latest_arrival = max(alice_arrive, bob_arrive)
        earliest_departure = min(alice_leave, bob_leave)
        if latest_arrival <= earliest_departure:
            return earliest_departure - latest_arrival + 1
        return 0