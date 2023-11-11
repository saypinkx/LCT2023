import React from 'react';
import { Alert, Box, Button, Paper, TextField, Typography } from '@mui/material';
import { useFormik } from 'formik';
import { object, string } from 'yup';
import { useAuth } from '@src/hooks';
import './login.less';

export const Login = (): React.ReactElement => {
  const { error, onLogin } = useAuth();
  const { errors, handleBlur, handleChange, handleSubmit, isValid, touched, values } = useFormik({
    initialValues: { username: '', password: '' },
    validationSchema: object({
      username: string().required('Введите логин'),
      password: string().required('Введите пароль'),
    }),
    onSubmit: onLogin,
  });

  return (
    <Box className="login">
      <Paper className="login-container" elevation={10}>
        <Typography component="h1" variant="h5">Войти</Typography>
        <Box component="form" onSubmit={handleSubmit} noValidate>
          <TextField
            autoComplete="username"
            error={touched.username && !!errors.username}
            fullWidth
            helperText={(touched.username && errors.username) ?? ''}
            id="username"
            label="Логин"
            name="username"
            onBlur={handleBlur}
            onChange={handleChange}
            sx={{ mt: 3 }}
            value={values.username}
            variant="outlined"
          />
          <TextField
            autoComplete="password"
            error={touched.password && !!errors.password}
            id="password"
            fullWidth
            helperText={(touched.password && errors.password) ?? ''}
            label="Пароль"
            name="password"
            onBlur={handleBlur}
            onChange={handleChange}
            sx={{ mt: 3 }}
            type="password"
            value={values.password}
            variant="outlined"
          />
          <Button disabled={!isValid} type="submit" variant="contained">Войти</Button>
        </Box>
        {error && (
          <Box sx={{ minWidth: 150, pt: 3 }}>
            <Alert severity="error">{error}</Alert>
          </Box>
        )}
      </Paper>
    </Box>
  );
};
