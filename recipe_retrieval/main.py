import requests
import csv


def recipe_search(search_items, page):
    # page = 0, 1 , 2 , 3, 4, 5
    # start = 0, 10, 20, 30, 40, 50
    # to = 10, 20, 30, 40, 50, 60
    app_id = '3a60ff17'
    app_key = 'b222ff4b6f73b945fd659232b9d7f5a5'
    start = page * 50
    to = start + 50
    result = requests.get('https://api.edamam.com/search?q={}&app_id={}&app_key={}&from={}&to={}'.format(search_items, app_id, app_key, start, to))
    status = result.status_code
    # print(status)
    data = result.json()
    if status != 200:
      print(
            'Error: request limit exceeded. Please wait and try again.')
    return data

def run():
    ingredient = input('Enter an ingredient to find recipes: ')
    meal_type = input('Enter meal type? (Breakfast, Lunch, Dinner, Teatime or Snack): ')
    healthlabel_list = [' balanced,', ' high-fiber,', ' high-protein,', ' low-carb,', ' low-fat,', ' alcohol-free,', ' immuno-supportive,', ' crustacean-free,', ' dairy-free,', ' egg-free,', ' fish-free,', ' fomap-free,', ' gluten-free,', ' key-friendly,', ' kidney-friendly,', ' kosher,', ' low-potassium,', ' lupine-free,', ' mustard-free,', ' low-fat-abs,', ' no-oil-added,', ' low-sugar,', ' paleo,', ' peanut-free,', ' pecatarian,', ' pork-free,', ' red-meat-free,', ' sesame-free,',' shellfish-free,', ' soy-free,', ' sugar-conscious,', ' tree-nut-free,', ' vegan,', ' vegetarian,', ' wheat-free']
    for hea in healthlabel_list[0:6]:
        print(hea, end=' ')
    print()
    for hea in healthlabel_list[6:12]:
        print(hea, end=' ')
    print()
    for hea in healthlabel_list[12:18]:
        print(hea, end=' ')
    print()
    for hea in healthlabel_list[18:24]:
        print(hea, end=' ')
    print()
    for hea in healthlabel_list[24:30]:
        print(hea, end=' ')
    print()
    for hea in healthlabel_list[30:]:
        print(hea, end=' ')
    print()
    health = input('Enter dietary requirements from the list above or enter none: ')
    search_items = '{}&mealType={}&healthLabels={}'.format(ingredient, meal_type, health)
    page = 0
    results = recipe_search(search_items, page)
    print('Total recipes for search {}, {} and {}: {}.'.format(ingredient, meal_type, health, results['count']))
    create_csv = input('Save results to file? y/n ')
    if create_csv == 'y':
      file_name ='{}.csv'.format(ingredient)      
      field_names = [
      'label', 
      'url', 
      'total_calories', 
      'servings'
      ]
      r = recipe_search(search_items, page)
      c = csv.writer(open(file_name, 'w+'), lineterminator='\n')
      c.writerow(field_names)
      for result in r['hits']:
        recipe = result['recipe']
        c.writerow([
         recipe['label'],
         recipe['shareAs'],
         recipe['calories'],
         recipe['yield']
        ])
    for result in results['hits']:
        recipe = result['recipe']
        print(recipe['label'])
        print(recipe['shareAs'])
        print(recipe['dietLabels'])
        print('This recipe serves {}. Calories per serving: {}'.format((int(recipe['yield'])), (int(int(recipe['calories'])/int(recipe['yield'])))))
        print('\n************************************************')
    # print('Total recipes for search {}, {} and {}: {}.'.format(ingredient, meal_type, health, results['count']))

    while results['more'] == True:
        page = page + 1
        results = recipe_search(search_items, page)
        for result in results['hits']:
            recipe = result['recipe']
            print(recipe['label'])
            print(recipe['shareAs'])
            print(recipe['dietLabels'])
            print('This recipe serves {}. Calories per serving: {}'.format((int(recipe['yield'])), (int(int(recipe['calories'])/int(recipe['yield'])))))
            print('\n************************************************')
        # print('Total recipes for search {}, {} and {}: {}'.format(ingredient, meal_type, health, results['count']))
            

    else:
      print('Basic account limited to first 100 results \nUpgrade to see more')
      
      


run()

