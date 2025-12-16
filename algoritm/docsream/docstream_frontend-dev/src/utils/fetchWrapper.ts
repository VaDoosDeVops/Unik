interface FetchOptions {
  method: 'GET' | 'POST' | 'PUT' | 'DELETE' | 'PATCH';
  headers?: any;
  body?: any;
}

export async function fetchApi(url: string, options: FetchOptions): Promise<any> {
  try {
    const headers = {
      ...options.headers,
    };
    if (!(options.body instanceof FormData)) {
      headers['Content-Type'] = 'application/json';
    }

    const response = await fetch(url, {
      method: options.method,
      headers,
      body: options.body instanceof FormData ? options.body : JSON.stringify(options.body),
    });
    if (response.ok) {
      return {
        status: response.status,
        headers: response.headers,
        response,
      };
    }
    const message = await response.text();
    return {
      status: response.status,
      message,
    };
  } catch (error) {
    return {
      status: 'error',
      message: (error as Error).message,
    };
  }
}
