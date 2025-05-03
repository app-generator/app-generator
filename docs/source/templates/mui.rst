MUI (Material UI)
=================

Material-UI (now known as MUI) is a popular React component library that implements Google's Material Design principles. 
It provides a comprehensive set of pre-built, customizable components to build modern, responsive web applications quickly.

.. include::  /_templates/components/banner-top.rst


Here's what makes MUI powerful:

- **Rich component library**: Includes buttons, inputs, navigation, data display, and more
- **Theming system**: Customize colors, typography, and spacing across your entire app
- **Responsive design**: Components adapt to different screen sizes automatically
- **Style customization**: Override styles using CSS-in-JS with emotion
- **Tree-shaking**: Only imports the components you use for smaller bundle sizes

A simple example of using MUI components:

.. code-block:: jsx 
   
   import React from 'react';
   import Button from '@mui/material/Button';
   import TextField from '@mui/material/TextField';
   import Box from '@mui/material/Box';

   function LoginForm() {
   return (
      <Box sx={{ maxWidth: 400, mx: 'auto', p: 2 }}>
         <TextField 
         fullWidth
         label="Email" 
         margin="normal" 
         variant="outlined" 
         />
         <TextField 
         fullWidth
         label="Password" 
         type="password" 
         margin="normal" 
         variant="outlined" 
         />
         <Button 
         variant="contained" 
         color="primary" 
         fullWidth 
         sx={{ mt: 2 }}
         >
         Log In
         </Button>
      </Box>
   );
   }


To set up a custom theme:

.. code-block:: jsx  

   import { createTheme, ThemeProvider } from '@mui/material/styles';

   const theme = createTheme({
   palette: {
      primary: {
         main: '#1976d2',
      },
      secondary: {
         main: '#dc004e',
      },
   },
   typography: {
      fontFamily: '"Roboto", "Helvetica", "Arial", sans-serif',
   },
   });

   function App() {
   return (
      <ThemeProvider theme={theme}>
         {/* Your app components */}
      </ThemeProvider>
   );
   }

.. include::  /_templates/components/footer-links.rst
