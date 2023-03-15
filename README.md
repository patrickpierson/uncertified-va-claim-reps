# Uncertified VA Claim Reps repo

## Uncertified Claim Reps
- vetassist.org - C seems linked to vetlinksolutions.com
- vaclaimsinsider.com - F-, free to join program. Payment comes after rating increase. 

## Certified lists from VA
- Attorneys - https://www.va.gov/ogc/apps/accreditation/attorneyexcellist.asp
- Claims Agents - https://www.va.gov/ogc/apps/accreditation/caexcellist.asp
- VSO Representatives - https://www.va.gov/ogc/apps/accreditation/repexcellist.asp - Data validation on VA's side needs work. Multiple entries with more columns then headers
- VSOs with Reps - https://www.va.gov/ogc/apps/accreditation/orgsexcellist.asp

## Details on Googling
#### Not going to name any names of groups I have found that were Certified. Just keeping track based on searches
- Uncertified - 2
- Certified - 3


## Grading Scale
- A - States that they are not certified and clearly states no payment required
- B - States that they are not certified and does not clearly state paymet method
- C - Uncertified and does not push you to contact them
- D - Uncertified and is not clearly identifiy payment structure
- F - Uncertified and clearly accepts payment by taking a portion of claim
- (minus) - For Ads on Google Searches

## Download.py
### Downloads VA Certified list and convers to CSV

#### Install
> pipenv --three
> pipenv install
> mkdir data

#### Run
> pipenv run python download.py

#### Use
> cat data/*csv | grep First | grep Last
This will enable you to search for someone's first as last name in the certified lists.