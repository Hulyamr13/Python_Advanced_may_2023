CREATE TRIGGER tr_deleted_employees
AFTER DELETE
ON employees
FOR EACH ROW
EXECUTE FUNCTION trigger_fn_on_employee_delete();
