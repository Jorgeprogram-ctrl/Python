def run(database: list) -> list:
    database_sorted = sorted(database, key=lambda x: x['id'])

    for index, record in enumerate(database_sorted):
        record['id'] = index + 1
    print(database_sorted)
    return database_sorted


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
