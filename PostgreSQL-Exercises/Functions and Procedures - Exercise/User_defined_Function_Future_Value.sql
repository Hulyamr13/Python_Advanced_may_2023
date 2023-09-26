CREATE OR REPLACE FUNCTION fn_calculate_future_value(
    initial_sum NUMERIC,
    yearly_interest_rate NUMERIC,
    number_of_years NUMERIC)
RETURNS VARCHAR
AS $$
BEGIN
    RETURN TO_CHAR(
        TRUNC(
            initial_sum * POWER(1 + yearly_interest_rate, number_of_years),
            4
        ),
        '9999999999999.9999'
    );
END;
$$ LANGUAGE plpgsql;