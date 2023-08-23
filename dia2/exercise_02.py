def unify_list(list):
    unified_list = []
    duplicates = []
    for i in range(0,len(list)):
        if list[i] not in unified_list:
            unified_list.append(list[i])
        else:
            if list[i] not in duplicates:
                duplicates.append(list[i])
    return unified_list,duplicates
def main():
    list = [1,1,1,2,3,4,4]
    unified_list,duplicates = unify_list(list)
    print(unified_list)
    print("Duplicates:",duplicates)
main()
