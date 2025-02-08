# Backend - Python

# Pay_for_beers

### 🚀 Funcionalidad Principal

El objetivo es generar 5 endpoint :

- Listar la cerveza disponible
- Listar amigos
- Recibir una orden
- Obtener la cuenta
- Pagar la cuenta. La cuenta puede dividirse entre los 3 amigos por igual. Este
  endpoint también debe permitirle a cada uno pagar lo que ordenó

1. **Listar la cerveza disponible (`list_beer`)**:

       - Se obtiene el listado de cervesas disponibles.

2. **Listar amigos (`list_friend`)**:

       - Se obtiene el listado de amigos.

3. **Recibir una orden (`place_order`)**:

       - Se realiza  la simulacion de realizar una orden por amigo donde un amigo realiza la orden donde solicita que cerveza y la cantidad.

4. **Obtener la cuenta (`get_account`)**:

       - Se realiza  la simulacion de obtener la cuenta por amigo , detallado lo que consumio.

5. **Pagar la cuenta (`pay_account`)**:

       - Se realiza  la simulacion de de pagar la cuenta donde si escogemos el split_equally true la cuenta se divide para 3 amigos en partes iguales y si es false solo sale la cuenta a pagar lo que consumio el amigo unicamente.

### 🛠️ Arquitectura

El sistema sigue una estructura modular para mantener la claridad y facilitar el mantenimiento.

1. **Components**:

       - Core: Contiene las entidades principales (`Order`, `Stock`, etc.) y lógica principal como `list_beer`,`list_friend`,`place_order`,`get_account`,`pay_account`.
       - Infrastructure: Se encarga de manejar los datos de entrada como inventario (`stock_data`).
       - Interfaces: Capa para controladores y comunicación entre capas (como `order_controller.py`).

2. **Flujo del Listar la cerveza disponible**:

       - Los datos del inventario (`stock_data`) se envían a al caso de uso 'list_beer'.
       - En lista todas las cervesas que tengan la cantidad mayor a 0

3. **Flujo del Listar amigos**:

       - Los datos del inventario (`stock_data`) se envían a al caso de uso 'list_friend'.
       - En lista todos los amigos dentro del stock_data

4. **Flujo del Recibir una orden**:

       - Los datos del inventario (`stock_data`), el nombre del amigo (`friend_name`), el nombre de la cervesa (`beer_name`), la cantidad de cervezas (`quantity`) se envían a al caso de uso 'place_order'.
       - la respuesta simulada es el amigo que solicito y la cerveza que solicito y la cantidad.

5. **Flujo del Obtener la cuentas**:

       - Los datos del inventario (`stock_data`), el nombre del amigo (`friend_name`) se envían a al caso de uso 'get_account'.
       - la respuesta simulada de lo que ordeno el amigo y la cantidad total que tiene que pagar y el detalle de lo que ordeno.

6. **Flujo del Pagar la cuentas**:

       - Los datos del inventario (`stock_data`), el nombre del amigo (`friend_name`) y escoger  true si la cuenta es dividida para 3 en partes iguales o false si solo es por amigo (`split_equally`) se envían a al caso de uso 'pay_account'.
       - la respuesta simulada de lo que debe pagar dependienso si desea compartida o separada.

### 🔧 Instalación

1. **Clonar el repositorio:**

       git clone git@github.com:beto-dt/Pay_for_beers.git

2. **Instalar dependencias:** Asegúrate de tener Python 3.10+ y usa `pip` para instalar las dependencias.

       pip3 install -r requirements.txt

3. **Ejecutar pruebas:** :

        uvicorn backend.app.main:app --reload

# Frontend - NextJs

# Pay_for_beers

### 🔧 Instalación

1. **Clonar el repositorio:**

       git clone git@github.com:beto-dt/Pay_for_beers.git
       cd frontend

2. **Instalar dependencias:**

       npm install

4. **Levantar proyecto:** :

       npm run dev

### 🔧 Observaciones

      Para poder levantar completamente el proyecto es necesario levantar el backend  y el frontend

      Creamos un archivo .env en la raiz del proyecto y su contenido debe ser 

      NEXT_PUBLIC_API_URL= http://localhost:8000