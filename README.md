# test_project
Тестовое задание

Создать 2 модели:
Channel
Name: String
Slug: String
BidTypes поддерживаемые конкретным каналом тип ставки на действие (cpc,cpm,cpa,cpv,cpi): array of strings
Campaign
Name: String
Channel: FK
Bid: Float
BidType (при сохранении кампании проверять что указанный BidType представлен в BidTypes канала): string

Реализовать представление этих моделей в API через django-rest-framework для CRUD операций. Аналогично сделать для Class based views.

Для канала в кампании сделать вложенный сериализатор на чтение.

Написать тесты на каждую операцию в АПИ и class based views.

Сделать вывод этих моделей в админке. Для канала сделать StackedInline по списку кампаний.
