from company import Company

for _ in range(10):
    company = Company()
    print('---------------')
    print(f'{company.name}{company.suffix}')
    print(f'  {company.url}')
    print(f'  {company.phone}')
    print(f'  {company.street_address}')
    print(f'  {company.city}, {company.state}')
    print(f'  Founded {company.founded} by {company.founder}')
