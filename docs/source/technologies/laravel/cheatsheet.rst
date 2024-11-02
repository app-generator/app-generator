Cheatsheet
==========

Laravel is a free, open-source PHP web framework created by Taylor Otwell in 2011. 
It follows the model-view-controller (MVC) architectural pattern and aims to make the development process more enjoyable for developers by simplifying common tasks used in many web projects.

.. include::  /_templates/components/banner-top.rst

**Routing and Controllers**

.. code-block:: php    

    // routes/web.php
    use App\Http\Controllers\UserController;

    // Basic routes
    Route::get('/', function () {
        return view('welcome');
    });

    // Route with parameters
    Route::get('/user/{id}', function ($id) {
        return 'User '.$id;
    });

    // Controller routes
    Route::get('/users', [UserController::class, 'index']);
    Route::resource('posts', PostController::class);

    // Route groups
    Route::middleware(['auth'])->group(function () {
        Route::get('/dashboard', function () {
            return view('dashboard');
        });
    });

    // Route with name
    Route::get('/profile', function () {
        return view('profile');
    })->name('profile');

    // Controller class
    class UserController extends Controller
    {
        public function index()
        {
            $users = User::all();
            return view('users.index', compact('users'));
        }

        public function show(User $user)
        {
            return view('users.show', compact('user'));
        }
    }
    

**Eloquent ORM and Database**

.. code-block:: php    

    // Model definition
    class User extends Model
    {
        protected $fillable = ['name', 'email', 'password'];

        // Relationships
        public function posts()
        {
            return $this->hasMany(Post::class);
        }

        public function profile()
        {
            return $this->hasOne(Profile::class);
        }
    }

    // Database queries
    // Basic CRUD
    $user = User::create([
        'name' => 'John Doe',
        'email' => 'john@example.com'
    ]);

    $users = User::where('active', true)->get();
    $user = User::find(1);
    $user->update(['name' => 'Jane Doe']);
    $user->delete();

    // Advanced queries
    $users = User::where('votes', '>', 100)
                ->orWhere('name', 'John')
                ->orderBy('name', 'desc')
                ->take(10)
                ->get();

    // Relationships
    $user->posts()->create([
        'title' => 'My Post'
    ]);

    // Eager loading
    $users = User::with('posts')->get();
    

**Blade Templates**

.. code-block:: php    

    // resources/views/layout.blade.php
    <!DOCTYPE html>
    <html>
    <head>
        <title>@yield('title')</title>
    </head>
    <body>
        @include('partials.header')

        @yield('content')

        @include('partials.footer')
    </body>
    </html>

    // resources/views/home.blade.php
    @extends('layout')

    @section('title', 'Home Page')

    @section('content')
        @if(auth()->check())
            <h1>Welcome, {{ auth()->user()->name }}</h1>
        @endif

        @foreach($posts as $post)
            <div class="post">
                <h2>{{ $post->title }}</h2>
                <p>{{ $post->content }}</p>
            </div>
        @endforeach

        @forelse($comments as $comment)
            <p>{{ $comment->body }}</p>
        @empty
            <p>No comments found.</p>
        @endforelse

        @component('components.alert')
            @slot('title')
                Alert Title
            @endslot
            <strong>Alert content here</strong>
        @endcomponent
    </body>
    </html>
    

**Authentication and Authorization**

.. code-block:: php    

    // Authentication
    use Illuminate\Support\Facades\Auth;

    // Login
    if (Auth::attempt(['email' => $email, 'password' => $password])) {
        return redirect()->intended('dashboard');
    }

    // Logout
    Auth::logout();

    // Get authenticated user
    $user = Auth::user();

    // Authorization (Policies)
    class PostPolicy
    {
        public function update(User $user, Post $post)
        {
            return $user->id === $post->user_id;
        }
    }

    // Using policies
    if ($user->can('update', $post)) {
        //
    }

    // Gates
    Gate::define('admin', function (User $user) {
        return $user->is_admin;
    });

    // Middleware
    Route::middleware(['auth'])->group(function () {
        // Protected routes
    });
    

**Form Validation**

.. code-block:: php    

    // Controller validation
    public function store(Request $request)
    {
        $validated = $request->validate([
            'title' => 'required|unique:posts|max:255',
            'body' => 'required',
            'email' => 'required|email',
            'age' => 'required|numeric|min:18',
        ]);

        // Create post with validated data
        Post::create($validated);
    }

    // Form Request Validation
    class StorePostRequest extends FormRequest
    {
        public function rules()
        {
            return [
                'title' => 'required|unique:posts|max:255',
                'body' => 'required',
            ];
        }

        public function messages()
        {
            return [
                'title.required' => 'A title is required',
                'body.required' => 'A message is required',
            ];
        }
    }

    // Using custom request in controller
    public function store(StorePostRequest $request)
    {
        $validated = $request->validated();
        // Store the post
    }
    

**API Development**

.. code-block:: php    

    // routes/api.php
    Route::middleware('auth:sanctum')->group(function () {
        Route::get('/user', function (Request $request) {
            return $request->user();
        });
        
        Route::apiResource('posts', PostController::class);
    });

    // API Controller
    class PostController extends Controller
    {
        public function index()
        {
            return PostResource::collection(Post::paginate());
        }

        public function store(Request $request)
        {
            $validated = $request->validate([
                'title' => 'required',
                'content' => 'required',
            ]);

            $post = Post::create($validated);
            
            return new PostResource($post);
        }
    }

    // API Resource
    class PostResource extends JsonResource
    {
        public function toArray($request)
        {
            return [
                'id' => $this->id,
                'title' => $this->title,
                'content' => $this->content,
                'created_at' => $this->created_at->toDateTimeString(),
            ];
        }
    }
    

**Events and Listeners**

.. code-block:: php    

    // Event class
    class OrderShipped extends Event
    {
        public $order;

        public function __construct(Order $order)
        {
            $this->order = $order;
        }
    }

    // Listener class
    class SendShipmentNotification
    {
        public function handle(OrderShipped $event)
        {
            // Send notification logic
        }
    }

    // EventServiceProvider
    protected $listen = [
        OrderShipped::class => [
            SendShipmentNotification::class,
        ],
    ];

    // Dispatching events
    event(new OrderShipped($order));
    // Or
    OrderShipped::dispatch($order);
    

**Queue Jobs**

.. code-block:: php    

    // Job class
    class ProcessPodcast implements ShouldQueue
    {
        use Dispatchable, InteractsWithQueue, Queueable, SerializesModels;

        private $podcast;

        public function __construct(Podcast $podcast)
        {
            $this->podcast = $podcast;
        }

        public function handle()
        {
            // Process the podcast
        }
    }

    // Dispatching jobs
    ProcessPodcast::dispatch($podcast);
    // Or with delay
    ProcessPodcast::dispatch($podcast)->delay(now()->addMinutes(10));

    // Job chaining
    ProcessPodcast::withChain([
        new OptimizePodcast,
        new ReleasePodcast
    ])->dispatch();
    

**Testing**

.. code-block:: php    

    // Feature test
    class PostTest extends TestCase
    {
        use RefreshDatabase;

        public function test_user_can_create_post()
        {
            $user = User::factory()->create();
            
            $response = $this->actingAs($user)->post('/posts', [
                'title' => 'Test Post',
                'content' => 'Test Content'
            ]);

            $response->assertStatus(201);
            $this->assertDatabaseHas('posts', [
                'title' => 'Test Post'
            ]);
        }
    }

    // Unit test
    class UserTest extends TestCase
    {
        public function test_user_has_full_name_attribute()
        {
            $user = User::factory()->create([
                'first_name' => 'John',
                'last_name' => 'Doe'
            ]);

            $this->assertEquals('John Doe', $user->full_name);
        }
    }
    

**Artisan Commands**

.. code-block:: php    

    // Custom command
    class SendEmails extends Command
    {
        protected $signature = 'mail:send {user} {--queue}';
        
        protected $description = 'Send emails to users';

        public function handle()
        {
            $userId = $this->argument('user');
            $queue = $this->option('queue');

            // Command logic
        }
    }

    // Common Artisan commands
    php artisan list                     # List commands
    php artisan make:model Post -mc      # Create model with migration and controller
    php artisan make:controller PostController --resource  # Resource controller
    php artisan migrate                  # Run migrations
    php artisan db:seed                  # Run seeders
    php artisan queue:work              # Start queue worker
    php artisan cache:clear             # Clear cache
    php artisan route:list              # List routes
    php artisan serve                   # Start development server
    

**Pro Tips**

- Use Laravel Sail for Docker development environment
- Implement repository pattern for large applications
- Use Laravel Telescope for debugging
- Implement proper error handling and logging
- Use Laravel Sanctum for API authentication
- Implement proper caching strategy
- Use Laravel Scout for full-text search
- Write comprehensive tests
- Use Laravel Horizon for queue monitoring
- Implement proper security measures
- Use Laravel Mix for asset compilation
- Keep controllers thin and use service classes 

.. include::  /_templates/components/footer-links.rst
