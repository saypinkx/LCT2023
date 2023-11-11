import React from 'react';
import { Box, Button, FormControl, FormHelperText, InputLabel, MenuItem, Modal, Select, TextField, Typography } from '@mui/material';
import { postMaterial, putMaterial } from '@src/api';
import { Folder, Material } from '@src/models';
import { useFormik } from 'formik';
import { object, string } from 'yup';
import './material-edit.less';

interface MaterialEditProps {
  folders: Folder[];
  item: Material | null;
  onClose: (isSubmit: boolean) => void;
}

export const MaterialEdit = ({ folders, item, onClose }: MaterialEditProps): React.ReactElement => {
  const { dirty, errors, handleBlur, handleChange, handleSubmit, isValid, setFieldValue, touched, values } = useFormik({
    initialValues: {
      folder_id: item?.folder_id ?? null,
      name: item?.name ?? '',
      link: item?.link ?? '',
    },
    validationSchema: object({
      folder_id: string().required('Выберите директорию'),
      name: string().required('Введите наименование'),
    }),
    onSubmit: body => {
      (item ? putMaterial(item.id, body) : postMaterial(body))
        .then(() => onClose(true))
        .catch(console.log);
    },
  });

  return (
    <Modal open onClose={onClose.bind(null, false)}>
      <div className="material-edit">
        <Typography variant="h6" component="h2">
          {item ? 'Изменить материал' : 'Добавить материал'}
        </Typography>
        <Box component="form" onSubmit={handleSubmit} noValidate>
          <FormControl error={!!errors.folder_id} fullWidth required sx={{ marginTop: 3 }}>
            <InputLabel id="directory-label">Директория</InputLabel>
            <Select
              fullWidth
              id="directory"
              label="Директория"
              labelId="directory"
              onBlur={handleBlur}
              onChange={event => {
                handleChange(event);
                setFieldValue('folder_id', event.target.value);
              }}
              value={values.folder_id ?? ''}
            >
              <MenuItem key="null" value={null}>Не выбрано</MenuItem>
              {folders.map(option => (
                <MenuItem key={`${option.id}`} value={option.id}>{option.name}</MenuItem>
              ))}
            </Select>
            {errors.folder_id && <FormHelperText>{errors.folder_id}</FormHelperText>}
          </FormControl>
          <TextField
            autoComplete="name"
            error={touched.name && !!errors.name}
            fullWidth
            helperText={(touched.name && errors.name) ?? ''}
            id="name"
            label="Наименование"
            name="name"
            onBlur={handleBlur}
            onChange={handleChange}
            required
            sx={{ mt: 3 }}
            value={values.name}
            variant="outlined"
          />
          <TextField
            autoComplete="link"
            error={touched.link && !!errors.link}
            id="link"
            fullWidth
            helperText={(touched.link && errors.link) ?? ''}
            label="Ссылка"
            name="link"
            onBlur={handleBlur}
            onChange={handleChange}
            sx={{ mt: 3 }}
            value={values.link}
            variant="outlined"
          />
          <div className="material-edit-options">
            <Button color="primary" disabled={!dirty || !isValid} type="submit" variant="contained">
              Подтвердить
            </Button>
            <Button color="info" type="button" variant="contained" onClick={onClose.bind(null, false)}>
              Отменить
            </Button>
          </div>
        </Box>
      </div>
    </Modal>
  )
};
