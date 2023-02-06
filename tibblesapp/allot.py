import re

days = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY']
slot_hours = [None, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 3]

def remove_overlap(tt, slot):
    if 1 == int(slot[1]) or 2 == int(slot[1]):
        tt.pop((slot[0], 8), None)
    elif 3 == int(slot[1]) or 4 == int(slot[1]):
        tt.pop((slot[0], 9), None)
    elif 5 == int(slot[1]):
        tt.pop((slot[0], 10), None)
        tt.pop((slot[0], 12), None)
    elif 6 == int(slot[1]):
        tt.pop((slot[0], 10), None)
        tt.pop((slot[0], 11), None)
        tt.pop((slot[0], 12), None)
    elif 7 == int(slot[1]):
        tt.pop((slot[0], 11), None)
        tt.pop((slot[0], 12), None)
    elif 8 == int(slot[1]):
        tt.pop((slot[0], 1), None)
        tt.pop((slot[0], 2), None)
    elif 9 == int(slot[1]):
        tt.pop((slot[0], 3), None)
        tt.pop((slot[0], 4), None)
    elif 10 == int(slot[1]):
        tt.pop((slot[0], 5), None)
        tt.pop((slot[0], 6), None)
        tt.pop((slot[0], 11), None)
        tt.pop((slot[0], 12), None)
    elif 11 == int(slot[1]):
        tt.pop((slot[0], 7), None)
        tt.pop((slot[0], 6), None)
        tt.pop((slot[0], 10), None)
        tt.pop((slot[0], 12), None)
    elif 12 == int(slot[1]):
        tt.pop((slot[0], 5), None)
        tt.pop((slot[0], 7), None)
        tt.pop((slot[0], 6), None)
        tt.pop((slot[0], 10), None)
        tt.pop((slot[0], 11), None)

def check_adjacent(tt, slot, fac_id):
    if slot[1] == 1:
        if ((slot[0], 2) in tt.keys() and tt[(slot[0], 2)] is not None and tt[(slot[0], 2)][0] == fac_id):
            return True
    elif slot[1] == 2:
        if ((slot[0], 1) in tt.keys() and tt[(slot[0], 1)] is not None and tt[(slot[0], 1)][0] == fac_id)   \
        or ((slot[0], 9) in tt.keys() and tt[(slot[0], 9)] is not None and tt[(slot[0], 9)][0] == fac_id)   \
        or ((slot[0], 3) in tt.keys() and tt[(slot[0], 3)] is not None and tt[(slot[0], 3)][0] == fac_id):
            return True
    elif slot[1] == 3:
        if ((slot[0], 2) in tt.keys() and tt[(slot[0], 2)] is not None and tt[(slot[0], 2)][0] == fac_id)   \
        or ((slot[0], 8) in tt.keys() and tt[(slot[0], 8)] is not None and tt[(slot[0], 8)][0] == fac_id)   \
        or ((slot[0], 4) in tt.keys() and tt[(slot[0], 4)] is not None and tt[(slot[0], 4)][0] == fac_id):
            return True
    elif slot[1] == 4:
        if ((slot[0], 3) in tt.keys() and tt[(slot[0], 3)] is not None and tt[(slot[0], 3)][0] == fac_id)   \
        or ((slot[0], 5) in tt.keys() and tt[(slot[0], 5)] is not None and tt[(slot[0], 5)][0] == fac_id)   \
        or ((slot[0], 12) in tt.keys() and tt[(slot[0], 12)] is not None and tt[(slot[0], 12)][0] == fac_id)   \
        or ((slot[0], 10) in tt.keys() and tt[(slot[0], 10)] is not None and tt[(slot[0], 10)][0] == fac_id):
            return True
    elif slot[1] == 5:
        if ((slot[0], 4) in tt.keys() and tt[(slot[0], 4)] is not None and tt[(slot[0], 4)][0] == fac_id)   \
        or ((slot[0], 6) in tt.keys() and tt[(slot[0], 6)] is not None and tt[(slot[0], 6)][0] == fac_id)   \
        or ((slot[0], 11) in tt.keys() and tt[(slot[0], 11)] is not None and tt[(slot[0], 11)][0] == fac_id):
            return True
    elif slot[1] == 6:
        if ((slot[0], 5) in tt.keys() and tt[(slot[0], 5)] is not None and tt[(slot[0], 5)][0] == fac_id)   \
        or ((slot[0], 7) in tt.keys() and tt[(slot[0], 7)] is not None and tt[(slot[0], 7)][0] == fac_id):
            return True
    elif slot[1] == 7:
        if ((slot[0], 6) in tt.keys() and tt[(slot[0], 6)] is not None and tt[(slot[0], 6)][0] == fac_id)   \
        or ((slot[0], 10) in tt.keys() and tt[(slot[0], 10)] is not None and tt[(slot[0], 10)][0] == fac_id):
            return True
    elif slot[1] == 8:
        if ((slot[0], 3) in tt.keys() and tt[(slot[0], 3)] is not None and tt[(slot[0], 3)][0] == fac_id)   \
        or ((slot[0], 9) in tt.keys() and tt[(slot[0], 9)] is not None and tt[(slot[0], 9)][0] == fac_id):
            return True
    elif slot[1] == 9:
        if ((slot[0], 2) in tt.keys() and tt[(slot[0], 2)] is not None and tt[(slot[0], 2)][0] == fac_id)   \
        or ((slot[0], 12) in tt.keys() and tt[(slot[0], 12)] is not None and tt[(slot[0], 12)][0] == fac_id)   \
        or ((slot[0], 10) in tt.keys() and tt[(slot[0], 10)] is not None and tt[(slot[0], 10)][0] == fac_id):
            return True
    elif slot[1] == 10:
        if ((slot[0], 9) in tt.keys() and tt[(slot[0], 9)] is not None and tt[(slot[0], 9)][0] == fac_id)  \
        or ((slot[0], 4) in tt.keys() and tt[(slot[0], 4)] is not None and tt[(slot[0], 4)][0] == fac_id)   \
        or ((slot[0], 7) in tt.keys() and tt[(slot[0], 7)] is not None and tt[(slot[0], 7)][0] == fac_id) :
            return True
    elif slot[1] == 11:
        if ((slot[0], 5) in tt.keys() and tt[(slot[0], 5)] is not None and tt[(slot[0], 5)][0] == fac_id):
            return True
    return None

def is_lab(string):
    match = re.fullmatch(r"\b\w+[78]\b", string)
    if match != None:
        return string in match.group()
    else:
        return False

def find_subset(nums, target, start, subset):
    if target == 0:
        return subset
    for i in range(start, len(nums)):
        if nums[i] > target:
            continue
        res = find_subset(nums, target - nums[i], i + 1, subset + [nums[i]])
        if res:
            return res
    return []

def get_subset(nums, target):
    return find_subset(nums, target, 0, [])

def get_hours(pref_slot):
    sum = 0
    for i in range(len(pref_slot)):
        sum += slot_hours[pref_slot[i][1]]
    return sum

def reqslot(pref_slot, hours):
    req_slot = []
    slot_dur = []
    for i in pref_slot:
        slot_dur.append(slot_hours[i[1]])
    list = get_subset(slot_dur, hours)
    for i in list:
        for j in pref_slot:
            if slot_hours[j[1]] == i and j not in req_slot:
                req_slot.append(j)
                break
    return req_slot

def allot3 (sem3_info_tuple, sem3_slot_tuple):
    sem3_info = []
    for x in sem3_info_tuple:
        sem3_info.append(list(x))

    sem3_slot = []
    for x in sem3_slot_tuple:
        sem3_slot.append(list(x))

    #create a dictionary to hold timetable
    tt = {}
    for day in days:
        for slot in range(1, 13):
            tt[(day, slot)] = None
            
    #allot labs first 
    lab_sub = []       
    for x in sem3_info:
        if is_lab(x[1]):
            lab_sub.append(x) 
            for day in days:
                if (day, 12) in tt.keys() and tt[(day, 12)] is None:
                    tt[(day, 12)] = [x[0], x[1]]
                    remove_overlap(tt, (day, 12))
                    break

    #remove lab subjects
    for sub in lab_sub:
        sem3_info.remove(sub)
    del lab_sub
    del sub
    del day
    del slot

    is_alloted = []

    #remaining subjects alloted priority-wise
    for i in range(len(sem3_info)):
        is_alloted.append(False)
        #if subject is already present, continue
        if sem3_info[i][1] in tt.values():
            continue
        pref_slot = []
        #get the faculty's preferred slots
        for x in sem3_slot:     
            if sem3_info[i][0] == x[0]:
                pref_slot.append((x[1], x[2]))
        #if preferred slot is already taken, remove slot from preference
        #if preferred slot doesn't exist (due to overlap), remove slot from preference
        for slot in pref_slot:
            if (slot in tt.keys() and tt[slot] is not None) or slot not in tt.keys():
                pref_slot.remove(slot)   
        #get number of hours the faculty is available
        avail = get_hours(pref_slot)
        #if available hours is less than required hours, allot existing free slots 
        if avail < sem3_info[i][2]:
            for slot in pref_slot:
                if slot in tt.keys() and tt[slot] is None:
                    tt[slot] = [sem3_info[i][0], sem3_info[i][1]]
                    remove_overlap(tt, slot)
        #if faculty is available for more than required hours, find optimal slots and allocate
        elif avail > sem3_info[i][2]:
            req_slot = reqslot(pref_slot, sem3_info[i][2])
            for slot in req_slot:
                if slot in tt.keys() and tt[slot] is None:
                    tt[slot] = [sem3_info[i][0], sem3_info[i][1]]
                    remove_overlap(tt, slot)         
        #if available hours == required hours, then directly allot those slots
        elif avail == sem3_info[i][2]:
            for slot in pref_slot:
                if slot in tt.keys() and tt[slot] is None:
                    tt[slot] = [sem3_info[i][0], sem3_info[i][1]]
                    remove_overlap(tt, slot)

    # find out which subjects have not been alotted enough slots
    i = 0
    alloted_hours = []
    for tpl in sem3_info:
        alloc = []
        for item in tt.items():
            if item[1] is not None and tpl[1] in item[1]:
                alloc.append(item[0])
        alloted = get_hours(alloc)
        alloted_hours.append(alloted)
        if alloted == tpl[2]:
            is_alloted[i] = True
        i += 1

    #subjects which weren't allocated enough slots
    #allot slots for them
    for i in range(len(sem3_info)):
        if is_alloted[i] == True:
            continue
        else:        
            req_hours = sem3_info[i][2] - alloted_hours[i]
            while req_hours > 0:
                for day in days:
                    for slot in range(1, 12):
                        if (day, slot) in tt.keys() and tt[(day, slot)] is None   \
                        and get_hours([(day, slot)]) <= req_hours and    \
                        check_adjacent(tt, (day, slot), sem3_info[i][0]) is None:
                            tt[(day, slot)] = [sem3_info[i][0], sem3_info[i][1]]
                            remove_overlap(tt, (day, slot))
                            req_hours -= get_hours([(day, slot)])
    return tt

def check_clash(tt3, fac_id, slot):
    if slot in tt3.keys() and tt3[slot] is not None and fac_id == tt3[slot][0]:
        return True
    else:
        return False

def allot5 (sem5_info_tuple, sem5_slot_tuple, tt3):
    sem5_info = []
    for x in sem5_info_tuple:
        sem5_info.append(list(x))

    sem5_slot = []
    for x in sem5_slot_tuple:
        sem5_slot.append(list(x))

    #create a dictionary to hold timetable
    tt5 = {}
    for day in days:
        for slot in range(1, 13):
            tt5[(day, slot)] = None
            
    #allot labs first 
    lab_sub = []       
    for x in sem5_info:
        if is_lab(x[1]):
            lab_sub.append(x) 
            for day in days:
                if (day, 12) in tt5.keys() and tt5[(day, 12)] is None and not check_clash(tt3, x[0], (day, 12)):
                    tt5[(day, 12)] = [x[0], x[1]]
                    remove_overlap(tt5, (day, 12))
                    break

    #remove lab subjects
    for sub in lab_sub:
        sem5_info.remove(sub)
    del lab_sub
    del sub
    del day
    del slot

    is_alloted = []

    #remaining subjects alloted priority-wise
    for i in range(len(sem5_info)):
        is_alloted.append(False)
        #if subject is already present, continue
        if sem5_info[i][1] in tt5.values():
            continue
        pref_slot = []
        #get the faculty's preferred slots
        for x in sem5_slot:     
            if sem5_info[i][0] == x[0]:
                pref_slot.append((x[1], x[2]))
        #if preferred slot is already taken, remove slot from preference
        #if preferred slot doesn't exist (due to overlap), remove slot from preference
        #or if there is clash with 3rd sem timetable
        for slot in pref_slot:
            if (slot in tt5.keys() and tt5[slot] is not None) or slot not in tt5.keys() or check_clash(tt3, sem5_info[i][0], slot):
                pref_slot.remove(slot)   
        #get number of hours the faculty is available
        avail = get_hours(pref_slot)
        #if available hours is less than required hours, allot existing free slots 
        if avail < sem5_info[i][2]:
            for slot in pref_slot:
                if slot in tt5.keys() and tt5[slot] is None:
                    tt5[slot] = [sem5_info[i][0], sem5_info[i][1]]
                    remove_overlap(tt5, slot)
        #if faculty is available for more than required hours, find optimal slots and allocate
        elif avail > sem5_info[i][2]:
            req_slot = reqslot(pref_slot, sem5_info[i][2])
            for slot in req_slot:
                if slot in tt5.keys() and tt5[slot] is None:
                    tt5[slot] = [sem5_info[i][0], sem5_info[i][1]]
                    remove_overlap(tt5, slot)         
        #if available hours == required hours, then directly allot those slots
        elif avail == sem5_info[i][2]:
            for slot in pref_slot:
                if slot in tt5.keys() and tt5[slot] is None:
                    tt5[slot] = [sem5_info[i][0], sem5_info[i][1]]
                    remove_overlap(tt5, slot)

    # find out which subjects have not been alott5ed enough slots
    i = 0
    alloted_hours = []
    for tpl in sem5_info:
        alloc = []
        for item in tt5.items():
            if item[1] is not None and tpl[1] in item[1]:
                alloc.append(item[0])
        alloted = get_hours(alloc)
        alloted_hours.append(alloted)
        if alloted == tpl[2]:
            is_alloted[i] = True
        i += 1

    #subjects which weren't allocated enough slots
    #allot slots for them
    for i in range(len(sem5_info)):
        if is_alloted[i] == True:
            continue
        else:        
            req_hours = sem5_info[i][2] - alloted_hours[i]
            while req_hours > 0:
                for day in days:
                    for slot in range(1, 12):
                        if (day, slot) in tt5.keys() and tt5[(day, slot)] is None   \
                        and get_hours([(day, slot)]) <= req_hours and   \
                        not check_clash(tt3, sem5_info[i][0], (day, slot)) and  \
                        check_adjacent(tt5, (day, slot), sem5_info[i][0]) is None:
                            tt5[(day, slot)] = [sem5_info[i][0], sem5_info[i][1]]
                            remove_overlap(tt5, (day, slot))
                            req_hours -= get_hours([(day, slot)])
                            break 
    return tt5

