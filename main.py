import requests

# Funkcja pobierająca wydarzenia na podstawie tagu
def get_events_by_date(date):
    # Przygotowanie endpointu do filtrowania wydarzeń po tagu
    events_endpoint = f'{base_url}/events/filter/?tag={date}'

    # Wysłanie żądania GET
    response = requests.get(events_endpoint, headers=headers)

    if response.status_code == 200:
        events = response.json()
        if events:
            for event in events:
                print(f"ID: {event['id']}")
                print(f"Nazwa: {event['name']}")
                print(f"Data rozpoczęcia: {event['start_time']}")
                print(f"Czas trwania: {event['duration']} godzin")
                print(f"Opis: {event['short_description']}")
                print("Tagi: " + ", ".join([tag['name'] for tag in event['tags']]))
                print("-" * 40)
        else:
            print(f'Brak wydarzeń dla tagu: {tag_name}.')
    else:
        print(f'Błąd: {response.status_code} - Nie udało się pobrać danych.')



# Funkcja pobierająca wydarzenia na podstawie tagu
def get_events_by_tag(tag_name):
    # Przygotowanie endpointu do filtrowania wydarzeń po tagu
    events_endpoint = f'{base_url}/events/filter/?tag={tag_name}'

    # Wysłanie żądania GET
    response = requests.get(events_endpoint, headers=headers)

    if response.status_code == 200:
        events = response.json()
        if events:
            for event in events:
                print(f"ID: {event['id']}")
                print(f"Nazwa: {event['name']}")
                print(f"Data rozpoczęcia: {event['start_time']}")
                print(f"Czas trwania: {event['duration']} godzin")
                print(f"Opis: {event['short_description']}")
                print("Tagi: " + ", ".join([tag['name'] for tag in event['tags']]))
                print("-" * 40)
        else:
            print(f'Brak wydarzeń dla tagu: {tag_name}.')
    else:
        print(f'Błąd: {response.status_code} - Nie udało się pobrać danych.')


def get_event_by_id(event_id):
    event_endpoint = f'{base_url}/events/{event_id}'

    # Wysylanie zadania GET dla konkretnego wydarzenia
    response = requests.get(event_endpoint, headers=headers)

    if response.status_code == 200:
        event_details = response.json()
        print(f"ID: {event_details['id']}")
        print(f"Nazwa: {event_details['name']}")
        print(f"Data rozpoczęcia: {event_details['start_time']}")
        print(f"Czas trwania: {event_details['duration']} godzin")
        print(f"Lokalizacja: {event_details.get('location', 'Brak lokalizacji')}")
        print(f"Opis: {event_details['short_description']}")
        print(f"Pełny opis: {event_details['long_description']}")
        print(f"Link do rejestracji: {event_details.get('registration_link', 'Brak linku')}")
        print("Tagi: " + ", ".join([tag['name'] for tag in event_details['tags']]))
    else:
        print(f'Błąd: {response.status_code} - Nie udało się pobrać danych dla ID: {event_id}')


api_key = 'd7c88c42b025c8b51540ad6730c295a3'

base_url = 'https://rekrutacja.teamwsuws.pl'

events_endpoint = f'{base_url}/events/'

headers = {
    'api-key': api_key
}



get_event_by_id(6)
event_de


# Wysylanie zadania get
response = requests.get(events_endpoint, headers=headers)

if response.status_code == 200:
    events = response.json()


print(len(events))