# Ipswich Retail E-commerce Wireframes

## Page 1: Home Page (Product Catalog)

```
┌────────────────────────────────────────────────────────────────┐
│  IPSWICH RETAIL           [Search...]  [Cart] [Login/Signup]  │
├────────────────────────────────────────────────────────────────┤
│  Home | Products | About | Contact                            │
├────────────────────────────────────────────────────────────────┤
│                                                                │
│  ┌──────────────────────────────────────────────────────────┐ │
│  │         WELCOME TO IPSWICH RETAIL                        │ │
│  │         Your trusted online store                        │ │
│  └──────────────────────────────────────────────────────────┘ │
│                                                                │
│  Categories: [All] [Electronics] [Clothing] [Books] [Home]    │
│                                                                │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐     │
│  │  [IMG]   │  │  [IMG]   │  │  [IMG]   │  │  [IMG]   │     │
│  │          │  │          │  │          │  │          │     │
│  │ Product1 │  │ Product2 │  │ Product3 │  │ Product4 │     │
│  │  $99.99  │  │  $149.99 │  │  $79.99  │  │  $199.99 │     │
│  │ [Details]│  │ [Details]│  │ [Details]│  │ [Details]│     │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘     │
│                                                                │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐     │
│  │  [IMG]   │  │  [IMG]   │  │  [IMG]   │  │  [IMG]   │     │
│  │          │  │          │  │          │  │          │     │
│  │ Product5 │  │ Product6 │  │ Product7 │  │ Product8 │     │
│  │  $89.99  │  │  $129.99 │  │  $59.99  │  │  $299.99 │     │
│  │ [Details]│  │ [Details]│  │ [Details]│  │ [Details]│     │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘     │
│                                                                │
│                  [< Previous]  1 2 3  [Next >]                │
│                                                                │
├────────────────────────────────────────────────────────────────┤
│  Footer: About | Contact | Privacy | Terms                    │
│  © 2025 Ipswich Retail. All rights reserved.                  │
└────────────────────────────────────────────────────────────────┘
```

**Key Features:**
- Navigation bar with logo, search, cart icon (with badge), login/signup
- Category filter buttons
- Product grid (4 columns, responsive)
- Each product card shows: image, name, price, "View Details" button
- Pagination for browsing products
- Clean, simple Bootstrap-based design

---

## Page 2: Product Detail Page

```
┌────────────────────────────────────────────────────────────────┐
│  IPSWICH RETAIL           [Search...]  [Cart(2)] [User Menu]  │
├────────────────────────────────────────────────────────────────┤
│  Home > Products > Electronics > Product Name                 │
├────────────────────────────────────────────────────────────────┤
│                                                                │
│  ┌─────────────────────┐  ┌────────────────────────────────┐ │
│  │                     │  │  Product Name                   │ │
│  │                     │  │  Category: Electronics          │ │
│  │    PRODUCT IMAGE    │  │                                 │ │
│  │    (Large Photo)    │  │  Price: $149.99                │ │
│  │                     │  │                                 │ │
│  │                     │  │  In Stock: 25 units            │ │
│  │                     │  │                                 │ │
│  └─────────────────────┘  │  Description:                   │ │
│                           │  Lorem ipsum dolor sit amet,    │ │
│  [Thumb1] [Thumb2] [...]  │  consectetur adipiscing elit.  │ │
│                           │  Sed do eiusmod tempor         │ │
│                           │  incididunt ut labore et       │ │
│                           │  dolore magna aliqua.          │ │
│                           │                                 │ │
│                           │  Quantity: [- ] 1 [ +]         │ │
│                           │                                 │ │
│                           │  [   ADD TO CART   ]           │ │
│                           │  [ BUY NOW ]                    │ │
│                           └────────────────────────────────┘ │
│                                                                │
│  ┌──────────────────────────────────────────────────────────┐ │
│  │  PRODUCT SPECIFICATIONS                                  │ │
│  │  - Feature 1: Value                                      │ │
│  │  - Feature 2: Value                                      │ │
│  │  - Feature 3: Value                                      │ │
│  └──────────────────────────────────────────────────────────┘ │
│                                                                │
│  ┌──────────────────────────────────────────────────────────┐ │
│  │  RELATED PRODUCTS                                        │ │
│  │  [Product A]  [Product B]  [Product C]  [Product D]     │ │
│  └──────────────────────────────────────────────────────────┘ │
│                                                                │
├────────────────────────────────────────────────────────────────┤
│  Footer: About | Contact | Privacy | Terms                    │
└────────────────────────────────────────────────────────────────┘
```

**Key Features:**
- Breadcrumb navigation
- Large product image with thumbnail gallery
- Product information: name, category, price, stock status
- Detailed description
- Quantity selector (+ / - buttons)
- "Add to Cart" and "Buy Now" buttons
- Product specifications table
- Related products recommendations

---

## Page 3: Shopping Cart Page

```
┌────────────────────────────────────────────────────────────────┐
│  IPSWICH RETAIL           [Search...]  [Cart(3)] [User Menu]  │
├────────────────────────────────────────────────────────────────┤
│  Home > Shopping Cart                                         │
├────────────────────────────────────────────────────────────────┤
│                                                                │
│  YOUR SHOPPING CART                                           │
│                                                                │
│  ┌──────────────────────────────────────────────────────────┐ │
│  │ PRODUCT         QTY      PRICE      TOTAL      ACTION    │ │
│  ├──────────────────────────────────────────────────────────┤ │
│  │ [IMG] Product1   [- 2 +]  $99.99   $199.98   [Remove]   │ │
│  │ Electronics                                              │ │
│  ├──────────────────────────────────────────────────────────┤ │
│  │ [IMG] Product2   [- 1 +]  $149.99  $149.99   [Remove]   │ │
│  │ Gadgets                                                  │ │
│  ├──────────────────────────────────────────────────────────┤ │
│  │ [IMG] Product3   [- 3 +]  $79.99   $239.97   [Remove]   │ │
│  │ Accessories                                              │ │
│  └──────────────────────────────────────────────────────────┘ │
│                                                                │
│  ┌────────────────────┐  ┌────────────────────────────────┐  │
│  │ [← Continue        │  │  ORDER SUMMARY                 │  │
│  │    Shopping]       │  │                                │  │
│  │                    │  │  Subtotal:        $589.94     │  │
│  └────────────────────┘  │  Shipping:        $15.00      │  │
│                          │  Tax (10%):       $58.99      │  │
│                          │  ─────────────────────────     │  │
│                          │  TOTAL:           $663.93     │  │
│                          │                                │  │
│                          │  [  PROCEED TO CHECKOUT  →  ] │  │
│                          └────────────────────────────────┘  │
│                                                                │
│  ┌──────────────────────────────────────────────────────────┐ │
│  │  RECOMMENDED FOR YOU                                     │ │
│  │  [Product X]  [Product Y]  [Product Z]                  │ │
│  └──────────────────────────────────────────────────────────┘ │
│                                                                │
├────────────────────────────────────────────────────────────────┤
│  Footer: About | Contact | Privacy | Terms                    │
└────────────────────────────────────────────────────────────────┘
```

**Key Features:**
- Cart items table with product image, name, quantity controls, price, total
- Quantity increase/decrease buttons
- Remove item functionality
- "Continue Shopping" button
- Order summary sidebar: subtotal, shipping, tax, grand total
- "Proceed to Checkout" button
- Recommended products section
- Empty cart message if no items

---

## Page 4: Checkout / Order Confirmation Page

```
┌────────────────────────────────────────────────────────────────┐
│  IPSWICH RETAIL           [Search...]  [Cart(3)] [User Menu]  │
├────────────────────────────────────────────────────────────────┤
│  Home > Cart > Checkout                                       │
├────────────────────────────────────────────────────────────────┤
│                                                                │
│  CHECKOUT                                                     │
│                                                                │
│  ┌────────────────────────────┐  ┌──────────────────────────┐│
│  │ 1. SHIPPING INFORMATION    │  │  ORDER SUMMARY          ││
│  │                            │  │                          ││
│  │ Full Name:                 │  │  Items (3):     $589.94 ││
│  │ [________________]         │  │  Shipping:      $15.00  ││
│  │                            │  │  Tax:           $58.99  ││
│  │ Email:                     │  │  ─────────────────────  ││
│  │ [________________]         │  │  TOTAL:         $663.93 ││
│  │                            │  │                          ││
│  │ Phone:                     │  │  ┌──────────────────┐   ││
│  │ [________________]         │  │  │ [IMG] Product1  │   ││
│  │                            │  │  │ Qty: 2  $199.98 │   ││
│  │ Address:                   │  │  └──────────────────┘   ││
│  │ [________________]         │  │  ┌──────────────────┐   ││
│  │                            │  │  │ [IMG] Product2  │   ││
│  │ City:        Postal Code:  │  │  │ Qty: 1  $149.99 │   ││
│  │ [_______]    [_______]     │  │  └──────────────────┘   ││
│  │                            │  │  ┌──────────────────┐   ││
│  │ Country:                   │  │  │ [IMG] Product3  │   ││
│  │ [▼ Select Country]         │  │  │ Qty: 3  $239.97 │   ││
│  └────────────────────────────┘  │  └──────────────────┘   ││
│                                   └──────────────────────────┘│
│  ┌────────────────────────────┐                              │
│  │ 2. PAYMENT INFORMATION     │                              │
│  │                            │                              │
│  │ Payment Method:            │                              │
│  │ ○ Credit Card              │                              │
│  │ ○ Debit Card               │                              │
│  │ ○ Cash on Delivery         │                              │
│  │                            │                              │
│  │ Card Number:               │                              │
│  │ [____-____-____-____]      │                              │
│  │                            │                              │
│  │ Expiry:      CVV:          │                              │
│  │ [MM/YY]      [___]         │                              │
│  │                            │                              │
│  │ Cardholder Name:           │                              │
│  │ [________________]         │                              │
│  └────────────────────────────┘                              │
│                                                                │
│  [☑] I agree to terms and conditions                         │
│                                                                │
│  [← Back to Cart]           [  PLACE ORDER  ]                │
│                                                                │
├────────────────────────────────────────────────────────────────┤
│  Footer: About | Contact | Privacy | Terms                    │
└────────────────────────────────────────────────────────────────┘
```

**Key Features:**
- Two-column layout: checkout form + order summary
- Shipping information form: name, email, phone, address, city, postal code, country
- Payment information form: payment method selection, card details
- Order summary with item list and totals
- Terms and conditions checkbox
- "Back to Cart" and "Place Order" buttons
- Form validation
- Secure checkout badge/message

---

## Order Confirmation (After Checkout)

```
┌────────────────────────────────────────────────────────────────┐
│  IPSWICH RETAIL           [Search...]  [Cart(0)] [User Menu]  │
├────────────────────────────────────────────────────────────────┤
│                                                                │
│                  ┌────────────────────────┐                    │
│                  │          ✓             │                    │
│                  │  ORDER CONFIRMED!      │                    │
│                  └────────────────────────┘                    │
│                                                                │
│  Thank you for your order!                                    │
│                                                                │
│  Order Number: #ORD-2025-001234                               │
│  Order Date: Nov 13, 2025                                     │
│                                                                │
│  A confirmation email has been sent to: user@example.com      │
│                                                                │
│  ┌──────────────────────────────────────────────────────────┐ │
│  │  ORDER DETAILS                                           │ │
│  │                                                          │ │
│  │  Shipping to:                                            │ │
│  │  John Doe                                                │ │
│  │  123 Main Street, Ipswich                                │ │
│  │  IP1 1AA, United Kingdom                                 │ │
│  │                                                          │ │
│  │  Payment Method: Visa ending in 1234                     │ │
│  │                                                          │ │
│  │  Items Ordered:                                          │ │
│  │  - Product1 x 2 .................. $199.98              │ │
│  │  - Product2 x 1 .................. $149.99              │ │
│  │  - Product3 x 3 .................. $239.97              │ │
│  │                                                          │ │
│  │  Total: $663.93                                          │ │
│  │                                                          │ │
│  │  Estimated Delivery: Nov 18-20, 2025                     │ │
│  └──────────────────────────────────────────────────────────┘ │
│                                                                │
│  [← Continue Shopping]  [View Order Status]  [Print Receipt]  │
│                                                                │
├────────────────────────────────────────────────────────────────┤
│  Footer: About | Contact | Privacy | Terms                    │
└────────────────────────────────────────────────────────────────┘
```

---

## Design Notes

### Color Scheme
- **Primary**: Deep blue (#1a365d) - Trust, professional
- **Secondary**: Teal (#0d9488) - Modern, fresh
- **Accent**: Amber (#f59e0b) - CTA buttons, highlights
- **Background**: Off-white (#f9fafb)
- **Text**: Dark gray (#1f2937)

### Typography
- **Headers**: 'Poppins' - Clean, modern sans-serif
- **Body**: 'Inter' - Readable, professional
- **Prices**: Bold, larger font size for emphasis

### Responsive Design
- Desktop: 4-column product grid
- Tablet: 2-column product grid
- Mobile: 1-column product grid, stacked layout

### UI Components (Bootstrap 5)
- Navbar: Fixed top, transparent on scroll
- Cards: Shadow on hover for products
- Buttons: Rounded corners, smooth transitions
- Forms: Clear labels, validation states
- Icons: Bootstrap Icons or Font Awesome

### User Experience Principles
1. **Clear Navigation**: Always know where you are (breadcrumbs)
2. **Visual Feedback**: Cart badge updates, loading states
3. **Error Prevention**: Form validation, confirmation modals
4. **Consistency**: Same layout patterns across pages
5. **Accessibility**: Proper contrast, semantic HTML, ARIA labels

---

**Wireframe Version**: 1.0
**Created**: November 2025
**Tool**: ASCII/Text-based (to be converted to visual mockups using Draw.io/Figma)
