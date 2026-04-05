CREATE TABLE IF NOT EXISTS `project-fec042d1-2105-4fee-851.INTEGRATION.integration_prueba_tecnica` (
  postId INT64,
  id INT64,
  name STRING,
  email STRING,
  body STRING,
  load_datetime DATETIME
);

INSERT INTO `project-fec042d1-2105-4fee-851.INTEGRATION.integration_prueba_tecnica`
(postId, id, name, email, body, load_datetime)
WITH deduplicado AS (
  -- Deduplicamos registros por id dentro de la sandbox
  SELECT *,
         ROW_NUMBER() OVER(PARTITION BY id ORDER BY postId) AS rn
  FROM `project-fec042d1-2105-4fee-851.dataset_pruebatecnica.SANDBOX_PruebaTecnica`
)
SELECT d.postId, d.id, d.name, d.email, d.body, CURRENT_DATETIME() AS load_datetime
FROM deduplicado d
LEFT JOIN `project-fec042d1-2105-4fee-851.INTEGRATION.integration_prueba_tecnica` f
  ON d.id = f.id
WHERE d.rn = 1      -- Solo un registro por id desde la sandbox
  AND f.id IS NULL; -- Solo registros que no existen aún en la tabla final