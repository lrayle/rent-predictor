--  schema for block variables table and way to copy data
-- TODO: implement this. Copy block data.. 

DROP TABLE IF EXISTS block_vars;
CREATE TABLE block_vars
    (
    id bigserial primary key,
    varname1 int, -- fill these in. 
    varname2 real
    );

-- copy data
COPY block_vars(id,varname1,varname2)
    FROM 'path/to/ba_block_small.csv'
    DELIMITERS ',' CSV HEADER;