class round_robin():
    
    def __init__(self,process_ids,process_times=[]):
        self.process_ids = process_ids
        self.process_times = process_times
        self.waiting_times = [0]*len(self.process_times)
        if self.process_times != [] and (len(self.process_ids) != len(self.process_times)):
            raise ValueError("process ids not match with proces times")
    
    def get_waiting_times(self,time_period):
        t=0
        temp_times = list(self.process_times)
        while True:
            done = True
            for i, burst_time in enumerate(self.process_times):
                if temp_times[i] > 0:
                    done = False
                    if temp_times[i] > time_period:
                        t += time_period
                        temp_times[i] = temp_times[i] - time_period
                    else:
                        t += temp_times[i]
                        self.waiting_times[i] = t - burst_time
                        temp_times[i] = 0
            if done is True:
                return self.waiting_times

    def get_turnaround_times(self,time_period):
        return [wt+bt for wt,bt in zip(self.get_waiting_times(time_period),self.process_times)]
            
rr = round_robin(["p1","p2","p3"],[6,4,5])
print({pid:wt for pid,wt in zip(rr.process_ids,rr.get_waiting_times(2))})
print({pid:tat for pid,tat in zip(rr.process_ids,rr.get_turnaround_times(2))})
