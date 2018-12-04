# CORECT data API

## 1. Constraints

### 1.1 Iterms per Request

The maxium mutation number returned per request is 1,000,000.


### 1.2 IP address

All request should from USC inner IP address.



## 2. Responses
API sends a response as a JSON object.

~~~
{
   "status": "success/fail"
   "data": [ ... ],
   "format": "...",
   "header":[...],
   "next_page":""
}
~~~
## 3. Queries

The following table lists all API endpoints currently available at 

`http://206.189.218.218:5000/api`

|API endpoint| Description|
|------------|---------|
|`/`| Retrieve meta-information about dataset.|
|`/origin`| Retrieve  links for download origin files.|
|`/variant`|Query single variant by chromosomal position or identifier.|
|`/region`|Query all variants within a chromosomal region.|
|`/gene`|Query all variants within a gene.|
|`/batch`|Upload a querying file and do a batch querying job|

### 3.1 Get Original Data Files

To download all original data files, request the download url by 

`http://206.189.218.218:5000/api/origin`

**Return example:**

~~~
{"format":"links",
"data":
	["http://206.189.218.218:5000/api/download/1",
	"http://206.189.218.218:5000/api/download/2",
	...
}
~~~

### 3.2 Region query

To query all variants within a region, send `GET` request to 

`/api/region/`. The following table lists all supported parameters.

|Parameter | Required | Description |
|------------|---------|----|
|`chrom `| Yes|Chromosome name.|
|`start`| Yes |Chromosomal start position in base-pairs.|
|`end`| Yes |Chromosomal end position in base-pairs.|
|`header_id`|No|header id list. Seperated bu ` `|
**Examples:**

`/api/region/?chrom=chr1&start=100000&end=200000&header_id=1%2022%203%204`

~~~
{
    "data": [
        "2\t100008\t2:100008:T:A\tT\tA\t.\tPASS\t.\tintergenic\t.\t.\tENSG00000184731:ENST00000327669(dist=53623),ENSG00000227061:ENST00000437798(dist=97561)\t.\t.\t.\t.(0):intergenic(1)\tintergenic_region\tMODIFIER\t.\t.\t.\t.\tFAM110C-AC079779.7\tENSG00000184731-ENSG00000227061\tn.100008T>A\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\tFAM110C-AC079779.7(1):intergenic_region(1)\tintergenic_variant..."
    ],
    "format": "vcf"
}
~~~

### 3.3 Single variant query
To query a single variant, send `GET` request to 

`http://206.189.218.218:5000/api/variant`.The following table lists all supported parameters.

|Parameter | Required | Description |
|------------|---------|----|
|`chrom `| Yes|Chromosome name.|
|`pos`| Yes |Chromosomal position in base-pairs.|
|`ref`| No |Reference alle.|
|`alt`|No|Alternative alle|

**Examples:**

#### 3.3.1 	Find a variant 

`http://206.189.218.218:5000/api/variant?chrom=chr2&pos=100008&ref=T&alt=A`


#### 3.3.1 	Find all variants at a position 
`http://206.189.218.218:5000/api/variant?chrom=chr2&pos=100008`

### 3.4 Gene query

to do

### 3.5 Batch query
To query a batch of variants, send `POST` request to 

`http://206.189.218.218:5000/api/batch` along with a query file.The following table lists all supported parameters.

|Parameter | Required | Description |
|------------|---------|----|
|`tmp_file `| No|Chromosome name.|


#### 3.5.1 Query file foramt
#### 3.5.2 Request with parameter tmp file
#### 3.5.2 Request without parameter tmp file
## 4. R package
### 4.1 R package Installation
### 4.2 R package Usage
