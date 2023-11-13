# Real-estate-price-prediction

## Data source
https://data.milwaukee.gov/dataset/property-sales-data

## About Dataset
| Field Name    | Description                                                    | Type  |
|---------------|----------------------------------------------------------------|-------|
| PropertyID    | A unique identifier for each property.                         |  int64 |
| PropType      | The type of property (e.g., Commercial or Residential).        | Object |
| taxkey        | The tax key associated with the property.                      | Object |
| Address       | The address of the property.                                   | Object |
| CondoProject  | Information about whether the property is part of a condominium project (NaN indicates missing data). | Object  |
| District      | The district number for the property.                          | Object |
| nbhd          | The neighborhood number for the property.                      | Object |
| Style         | The architectural style of the property.                       | Object |
| Extwall       | The type of exterior wall material used.                       | Object |
| Stories       | The number of stories in the building.                         | float64 |
| Year_Built    | The year the property was built.                               |  int64 |
| Rooms         | The number of rooms in the property.                           | Object |
| FinishedSqft  | The total square footage of finished space in the property.    |  int64 |
| Units         | The number of units in the property (e.g., apartments in a multifamily building). | Object |
| Bdrms         | The number of bedrooms in the property.                        | Object |
| Fbath         | The number of full bathrooms in the property.                  | Object |
| Hbath         | The number of half bathrooms in the property.                  | Object |
| Lotsize       | The size of the lot associated with the property.              |  int64  |
| Sale_date     | The date when the property was sold.                           | datetime |
| Sale_price    | The sale price of the property.                                |  int64 |
