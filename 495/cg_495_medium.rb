# @param {Integer[]} time_series
# @param {Integer} duration
# @return {Integer}
def find_poisoned_duration(time_series, duration)
    time_poisoned = 0
    
    return 0 if time_series.length < 1
    
    for i in 1...time_series.length do
        time_poisoned += [time_series[i] - time_series[i - 1], duration].min
    end
    
    time_poisoned += duration
end
