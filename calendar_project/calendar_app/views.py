from django.shortcuts import render
import requests
from django.conf import settings
from django.http import JsonResponse
from datetime import datetime, timedelta


def calendar_view(request):
    return render(request, 'calendar_app/calendar.html')


def events_json(request):
    """Widok zwracający wydarzenia w formacie JSON dla FullCalendar"""
    api_key = settings.API_KEY
    base_url = settings.BASE_URL
    events_url = f'{base_url}/events/'

    headers = {'api-key': api_key}
    try:
        response = requests.get(events_url, headers=headers)
        response.raise_for_status()
        events = response.json()

        # Przekształć wydarzenia na format obsługiwany przez FullCalendar
        fullcalendar_events = []
        for event in events:
            # Konwertuje start_time na obiekt datetime
            start_time = datetime.fromisoformat(event['start_time'])

            # Obliczam czas zakończenia, dodając `duration` (zakładając, że duration jest w godzinach)
            end_time = start_time + timedelta(hours=event['duration'])

            fullcalendar_events.append({
                'title': event['name'],
                'start': start_time.isoformat(),
                'end': end_time.isoformat(),
                'extendedProps': {
                    'description': event['short_description'],
                    'duration': event['duration']
                    }
            })

    except requests.RequestException as e:
        fullcalendar_events = []

    return JsonResponse(fullcalendar_events, safe=False)